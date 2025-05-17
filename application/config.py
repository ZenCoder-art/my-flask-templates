import os


class BaseConfig:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/h5"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    pass


config = {
    "development": DevConfig,
    "production": ProdConfig,
    "testing": TestConfig,
}
