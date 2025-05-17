from flask import Flask

from application.config import config
from application.register import (
    register_bp,
    register_commands,
    register_extensions,
    register_middleware,
)


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(config["development"])
    # 初始化扩展
    register_extensions(app)
    # 初始化路由
    register_bp(app)
    # 初始化命令
    register_commands(app)
    # 初始化中间件
    register_middleware(app)
    return app
