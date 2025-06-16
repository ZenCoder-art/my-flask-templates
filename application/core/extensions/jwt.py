from flask_jwt_extended import JWTManager

from application.core.response import ResponseBuilder

jwt = JWTManager()


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return ResponseBuilder.error(
        code=401,
        message="token已过期",
        error_type=ResponseBuilder.response[401]["type"],
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return ResponseBuilder.error(
        code=401,
        message="无效的token",
        error_type=ResponseBuilder.response[401]["type"],
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return ResponseBuilder.error(
        code=401,
        message="缺少token",
        error_type=ResponseBuilder.response[401]["type"],
    )


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return ResponseBuilder.error(
        code=401,
        message="该token已进入黑名单,请联系客服解除",
        error_type=ResponseBuilder.response[401]["type"],
    )
