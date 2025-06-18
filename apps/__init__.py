from flask_openapi3 import Info, OpenAPI

from config import config
from register import (
    register_blueprints,
    register_commands,
    register_extensions,
    register_middleware,
)
from schema.response import (
    Forbidden,
    NotFound,
    ServerError,
    TooManyRequests,
    Unauthorized,
    ValidationError,
)


def create_application():
    info = Info(title="FlaskX API", version="1.0.0")
    security_schemes = {
        "jwt": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"},
        "api_key": {"type": "apiKey", "name": "X-API-KEY", "in": "header"},
    }
    app = OpenAPI(
        __name__,
        info=info,
        security_schemes=security_schemes,
        doc_prefix="/apidocs",
        doc_url="/openapi.json",
        responses={
            401: Unauthorized,
            403: Forbidden,
            404: NotFound,
            422: ValidationError,
            429: TooManyRequests,
            500: ServerError,
        },
    )
    app.config.from_object(config["development"])
    # 初始化路由
    register_blueprints(app)
    # 初始化扩展
    register_extensions(app)
    # 初始化中间件
    register_middleware(app)
    # 初始化命令
    register_commands(app)
    return app
