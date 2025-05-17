import importlib
import pkgutil

from application.core.commands import initdb
from application.core.extensions import cors, db, mail, migrate, siwa


def register_bp(app):
    routes_package = "application.routes"
    for _, module_name, _ in pkgutil.iter_modules([routes_package]):
        module_path = f"{routes_package}.{module_name}"
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, "bp"):
                bp = getattr(module, "bp")
                app.register_blueprint(bp)
        except Exception as e:
            continue


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    siwa.init_app(app)
    cors.init_app(app, resources=r"/*", origins="*", methods=["*"])
    mail.init_app(app)


def register_commands(app):
    app.cli.add_command(initdb)


def register_middleware(app):
    pass
