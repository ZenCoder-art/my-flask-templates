from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


class MigrateExtension:
    _instance = None
    migrate: Migrate

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.migrate = Migrate()
        return cls._instance

    def init_app(self, app: Flask, db: SQLAlchemy) -> None:
        self.migrate.init_app(app, db)
