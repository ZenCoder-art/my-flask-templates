from flask import Flask
from flask_mail import Mail


class MailExtension:
    _instance = None
    mail: Mail

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.mail = Mail()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.mail.init_app(app)
