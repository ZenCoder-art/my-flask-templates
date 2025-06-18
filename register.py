from apps.api import auth_bp
from apps.views import index_bp
from core.commands import initdb
from core.extensions import (
    CORSExtension,
    DBSessionExtension,
    JWTManagerExtension,
    MailExtension,
    MigrateExtension,
    RedisExtension,
)


def register_blueprints(app):
    app.register_blueprint(index_bp)
    # app.register_api(user_bp)
    app.register_api(auth_bp)
    # app.register_api(captcha_bp)


def register_extensions(app):
    # flask-migrate识别数据库模型
    from database.models import User

    DBSessionExtension().init_app(app)
    MigrateExtension().init_app(app, DBSessionExtension().db)
    CORSExtension().init_app(app)
    MailExtension().init_app(app)
    JWTManagerExtension().init_app(app)
    RedisExtension().init_app(app)
    # csrf.init_app(app)


def register_commands(app):
    app.cli.add_command(initdb)


def register_middleware(app):
    pass
