from flask import Flask
from flask_wtf.csrf import CSRFProtect


class CSRFExtension:
    _instance = None
    csrf: CSRFProtect

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.csrf = CSRFProtect()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.csrf.init_app(app)
