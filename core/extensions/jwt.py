from flask import Flask, redirect, url_for
from flask_jwt_extended import JWTManager

from core.response import ResponseBuilder


class JWTManagerExtension:
    _instance = None
    jwt: JWTManager

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.jwt = JWTManager()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.jwt.init_app(app)

        @self.jwt.expired_token_loader
        def expired_token_callback(jwt_header, jwt_payload):
            return ResponseBuilder.error(
                code=401,
                message="token已过期",
                error_type=ResponseBuilder.response[401]["type"],
            )

        @self.jwt.invalid_token_loader
        def invalid_token_callback(error):
            return ResponseBuilder.error(
                code=401,
                message="无效的token",
                error_type=ResponseBuilder.response[401]["type"],
            )

        @self.jwt.unauthorized_loader
        def missing_token_callback(error):
            return redirect(url_for("index.login"))

        @self.jwt.revoked_token_loader
        def revoked_token_callback(jwt_header, jwt_payload):
            return ResponseBuilder.error(
                code=401,
                message="该token已进入黑名单,请联系客服解除",
                error_type=ResponseBuilder.response[401]["type"],
            )
