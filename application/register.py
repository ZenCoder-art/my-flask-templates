import importlib
import pkgutil

from application.core.commands import initdb
from application.core.extensions import cors, db, init_siwa, jwt, mail, migrate, redis


def register_bp(app):
    routes_package = "application.routes"
    for _, module_name, _ in pkgutil.iter_modules([routes_package]):
        module_path = f"{routes_package}.{module_name}"
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "bp"):
                bp = getattr(module, "bp")
                app.register_blueprint(bp)
            else:
                raise ValueError(f"模块 {module_path} 没有 bp 属性")
        except Exception as e:
            continue


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    init_siwa(app).init_app(app)
    cors.init_app(
        app,
        resources=app.config["CORS_RESOURCES"],
        origins=app.config["CORS_ORIGINS"],
        methods=app.config["CORS_ALLOW_METHODS"],
        allow_headers=app.config["CORS_ALLOW_HEADERS"],
        supports_credentials=app.config["CORS_ALLOW_CREDENTIALS"],
    )
    mail.init_app(app)
    jwt.init_app(app)
    redis.init_app(app)


def register_commands(app):
    app.cli.add_command(initdb)


def register_middleware(app):
    pass
