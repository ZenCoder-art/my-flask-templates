import resend
from flask import Flask


class ResendExtension:
    _instance = None
    resend: resend

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.resend = resend.Resend()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.resend.api_key = app.config["RESEND_API_KEY"]
