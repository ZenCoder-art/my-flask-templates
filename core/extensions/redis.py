from flask import Flask
from flask_redis import FlaskRedis


class RedisExtension:
    _instance = None
    redis: FlaskRedis = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.redis = FlaskRedis()
        return cls._instance

    def init_app(self, app: Flask) -> None:
        self.redis.init_app(app)
