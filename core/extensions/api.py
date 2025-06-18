from flask import Flask
from flask_restful import Api

from .ext import BaseExtension


class APIExtension(BaseExtension):
    def __init__(self, enabled: bool = True) -> None:
        super().__init__(enabled)
        self.api: Api = Api()

    def _init_app(self, app: Flask) -> None:
        if self.enabled:
            self.api.init_app(app)
        else:
            pass
