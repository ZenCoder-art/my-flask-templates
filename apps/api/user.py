from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_openapi3 import APIBlueprint, Tag

from core.extensions import DBSessionExtension
from core.response import ResponseBuilder
from database.models import User
from schema import UserResetSchema

user_tag = Tag(name="User", description="用户相关接口")
user_bp = APIBlueprint(
    "/user",
    __name__,
    url_prefix="/api",
    abp_tags=[user_tag],
    abp_security=[{"jwt": []}],
)
db = DBSessionExtension().db


@user_bp.get(
    "/user",
    summary="获取用户信息",
)
@jwt_required()
def get_user():
    current_user_id = get_jwt_identity()
    token = request.headers.get("Authorization")
    user = User.query.get(current_user_id)
    if not user:
        return ResponseBuilder.error(
            code=404,
            message="用户不存在",
            error_type=ResponseBuilder.response[404]["type"],
        )
    return ResponseBuilder.success(
        code=200,
        message=ResponseBuilder.response[200]["message"],
        success_type=ResponseBuilder.response[200]["type"],
        data=user.to_dict() | {"token": token},
    )


@user_bp.delete("/user", tags=[user_tag], summary="删除用户")
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return ResponseBuilder.error(
            code=404,
            message="用户不存在",
            error_type=ResponseBuilder.response[404]["type"],
        )
    try:
        db.session.delete(user)
        db.session.commit()
        return ResponseBuilder.success(
            code=204,
            message=ResponseBuilder.response[204]["message"],
            success_type=ResponseBuilder.response[204]["type"],
        )
    except Exception as e:
        db.session.rollback()
        return ResponseBuilder.error(
            code=500,
            message=ResponseBuilder.response[500]["message"],
            error_type=ResponseBuilder.response[500]["type"],
            details=str(e),
        )


@user_bp.put("/user", summary="修改用户密码")
@jwt_required()
def change_password(body: UserResetSchema):
    old_password = body.old_password
    new_password = body.new_password
    if not old_password or not new_password:
        return ResponseBuilder.error(
            code=400,
            message=ResponseBuilder.response[400]["message"],
            error_type=ResponseBuilder.response[400]["type"],
        )
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user or not user.verify_password(old_password):
        return ResponseBuilder.error(
            code=401,
            message=ResponseBuilder.response[401]["message"],
            error_type=ResponseBuilder.response[401]["type"],
        )
    try:
        user.set_password(body.new_password)
        db.session.commit()
        return ResponseBuilder.success(
            code=200,
            message="密码修改成功",
            success_type=ResponseBuilder.response[200]["type"],
        )
    except Exception as e:
        db.session.rollback()
        return ResponseBuilder.error(
            code=500,
            message=ResponseBuilder.response[500]["message"],
            error_type=ResponseBuilder.response[500]["type"],
            details=str(e),
        )
