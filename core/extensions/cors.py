from flask import Flask
from flask_cors import CORS


class CORSExtension:
    _instance = None
    cors: CORS

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cors = CORS()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.cors.init_app(
            app,
            resources=app.config["CORS_RESOURCES"],
            origins=app.config["CORS_ORIGINS"],
            methods=app.config["CORS_ALLOW_METHODS"],
            allow_headers=app.config["CORS_ALLOW_HEADERS"],
            supports_credentials=app.config["CORS_ALLOW_CREDENTIALS"],
        )
