import hashlib
import uuid
from datetime import datetime
from io import BytesIO

from captcha.image import ImageCaptcha
from flask import current_app, send_file
from flask_openapi3 import APIBlueprint, Tag

from core.extensions import redis
from core.response import ResponseBuilder
from schema import CaptchaVerifySchema, EmailSchema, EmailVerifySchema
from schema.response import (
    Forbidden,
    NotFound,
    ServerError,
    SuccessResponse,
    TooManyRequests,
    Unauthorized,
    ValidationError,
)
from utils.tools import (
    random_number,
    resend_send_verification_email,
    smtp_send_verification_email,
)

captcha_tag = Tag(name="captcha", description="验证相关接口")
captcha_bp = APIBlueprint(
    "/captcha",
    __name__,
    url_prefix="/api",
    abp_tags=[captcha_tag],
    abp_responses={
        200: SuccessResponse,
        401: Unauthorized,
        403: Forbidden,
        404: NotFound,
        422: ValidationError,
        429: TooManyRequests,
        500: ServerError,
    },
)


@captcha_bp.post("/email/send_code")
def send_code(body: EmailSchema):
    email = body.email
    method = body.method
    subject = body.subject
    sender = body.sender
    if not email:
        return ResponseBuilder.error(
            code=400,
            message="邮箱地址不能为空",
            error_type=ResponseBuilder.response[400]["type"],
        )
    code = random_number(length=6)
    redis.setex(f"email_code:{email}", 600, code)
    if method == "smtp":
        smtp_send_verification_email(
            to_email=email,
            code=code,
            subject=subject,
            sender=sender,
            from_email=current_app.config["MAIL_DEFAULT_SENDER"],
        )
    elif method == "resend":
        resend_send_verification_email(
            to_email=email,
            code=code,
            subject=subject,
            sender=sender,
            from_email=current_app.config["RESEND_SENDER"],
        )
    else:
        return ResponseBuilder.error(
            code=400,
            message="不支持该发送邮件的方式",
            error_type=ResponseBuilder.response[400]["type"],
        )
    return ResponseBuilder.success(
        code=200,
        message="发送验证码成功",
        success_type=ResponseBuilder.response[200]["type"],
        data={
            "email": email,
            "method": method,
            "sent_at": datetime.now().isoformat() + "Z",
        },
    )


@captcha_bp.post("/email/verify_code")
def verify_code(body: EmailVerifySchema):
    email = body.email
    code = body.code
    redis_key = f"email_code:{email}"
    stored_code = redis.get(redis_key)
    if stored_code is None:
        return ResponseBuilder.error(
            code=400,
            message="验证码已过期",
            error_type=ResponseBuilder.response[400]["type"],
        )
    if stored_code.decode() != code:
        return ResponseBuilder.error(
            code=400,
            message="验证码错误",
            error_type=ResponseBuilder.response[400]["type"],
        )
    redis.delete(redis_key)
    return ResponseBuilder.success(
        code=200,
        message="验证码验证成功",
        success_type=ResponseBuilder.response[200]["type"],
    )


@captcha_bp.get("/image/captcha")
def get_captcha():
    raw_code = random_number(current_app.config.get("CAPTCHA_LEN", 4))
    ttl = current_app.config.get("CAPTCHA_TTL", 180)
    captcha_id = uuid.uuid4().hex
    hashed = hashlib.sha256(raw_code.encode()).hexdigest()
    redis.setex(f"captcha:{captcha_id}", ttl, hashed)
    buf = BytesIO()
    image = ImageCaptcha(width=160, height=60).write(raw_code, buf)
    buf.seek(0)
    response = send_file(
        buf,
        mimetype="image/png",
        download_name=f"{captcha_id}.png",
        max_age=0,
        conditional=False,
    )
    response.headers["Captcha-ID"] = captcha_id
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    return response


@captcha_bp.post("/image/verify_captcha")
def verify_captcha(form: CaptchaVerifySchema):
    captcha_id = form.captcha_id
    user_input = form.code
    stored_hash = redis.get(f"captcha:{captcha_id}")
    if not stored_hash:
        return ResponseBuilder.error(
            code=400,
            message="验证码已过期或不存在",
            error_type=ResponseBuilder.response[400]["type"],
        )
    input_hash = hashlib.sha256(user_input.encode()).hexdigest()
    if stored_hash.decode() != input_hash:
        return ResponseBuilder.error(
            code=400,
            message="验证码错误",
            error_type=ResponseBuilder.response[400]["type"],
        )
    redis.delete(f"captcha:{captcha_id}")
    return ResponseBuilder.success(
        code=200,
        message="验证码验证成功",
        success_type=ResponseBuilder.response[200]["type"],
    )
