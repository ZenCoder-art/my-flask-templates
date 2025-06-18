import re
from datetime import datetime

from flask import current_app
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from flask_openapi3 import APIBlueprint, Tag

from core.extensions import DBSessionExtension
from core.response import ResponseBuilder
from database.models import User
from schema import LoginSchema, RegisterSchema
from schema.response import (
    Forbidden,
    NotFound,
    ServerError,
    SuccessResponse,
    TooManyRequests,
    Unauthorized,
    ValidationError,
)

auth_tag = Tag(name="Auth", description="认证相关接口")
auth_bp = APIBlueprint(
    "/auth",
    __name__,
    url_prefix="/api",
    abp_tags=[auth_tag],
    abp_security=[
        {"api_key": []},
    ],
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
db = DBSessionExtension().db


@auth_bp.post("/auth/login", summary="用户登录")
def login(body: LoginSchema):
    identifier = body.username
    password = body.password
    if re.match(r"[^@]+@[^@]+\.[^@]+", identifier):
        user = User.query.filter_by(email=identifier).first()
    else:
        user = User.query.filter_by(username=identifier).first()
    if not user:
        return ResponseBuilder.error(
            code=404,
            message=ResponseBuilder.response[404]["message"],
            error_type=ResponseBuilder.response[404]["type"],
        )
    if not user.verify_password(password):
        return ResponseBuilder.error(
            code=403,
            message=ResponseBuilder.response[403]["message"],
            error_type=ResponseBuilder.response[403]["type"],
        )
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    token = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
    }
    return ResponseBuilder.success(
        code=200,
        message=ResponseBuilder.response[200]["message"],
        success_type=ResponseBuilder.response[200]["type"],
        data=user.to_dict() | token,
    )


@auth_bp.post("/auth/register", summary="用户注册")
def register(body: RegisterSchema):
    username = body.username
    email = body.email
    password = body.password
    if User.query.filter_by(username=username).first():
        return ResponseBuilder.error(
            code=400,
            message="用户名已存在",
            error_type=ResponseBuilder.response[400]["type"],
        )
    if User.query.filter_by(email=email).first():
        return ResponseBuilder.error(
            code=400,
            message="该邮箱已注册",
            error_type=ResponseBuilder.response[400]["type"],
        )
    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return ResponseBuilder.success(
            message=ResponseBuilder.response[201]["message"],
            success_type=ResponseBuilder.response[201]["type"],
            code=201,
            data=new_user.to_dict(),
        )
    except Exception as e:
        db.session.rollback()
        return ResponseBuilder.error(
            code=500,
            message=ResponseBuilder.response[500]["message"],
            error_type=ResponseBuilder.response[500]["type"],
            details=str(e),
        )


@auth_bp.route("/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    expires_delta = current_app.config.get("JWT_ACCESS_TOKEN_EXPIRES")
    expires_in = int(expires_delta.total_seconds())
    now = int(datetime.now().timestamp())
    return ResponseBuilder.success(
        code=200,
        message=ResponseBuilder.response[200]["message"],
        success_type=ResponseBuilder.response[200]["type"],
        data={
            "access_token": access_token,
            "token_type": "Bearer",
            "expires_in": expires_in,
            "issued_at": now,
            "user_id": user_id,
        },
    )


@auth_bp.route("/auth/logout", methods=["POST"])
@jwt_required()
def logout():
    pass
