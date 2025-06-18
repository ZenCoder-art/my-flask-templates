from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class DBSessionExtension:
    _instance = None
    db: SQLAlchemy

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = SQLAlchemy()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.db.init_app(app)
