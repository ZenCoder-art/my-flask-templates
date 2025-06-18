import os
from datetime import timedelta
from typing import ClassVar, List

from dotenv import find_dotenv, load_dotenv


class BaseConfig:
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    PROJECT_PATH: str = os.path.dirname(os.path.abspath(__file__))
    # 项目信息
    VERSION: str = "1.0.0"
    TITLE: str = "FlaskX的接口列表"
    DESCRIPTION: str = (
        '接口详细文档可以参考:<a href="/docs?ui=redoc" target="_blank">redoc</a><br/>接口JSON文档可以参考:<a href="/openapi.json" target="_blank">openapi</a>'
    )
    # 认证信息
    JWT_SECRET_KEY: str = "JWT_SECRET_KEY"
    JWT_ACCESS_TOKEN_EXPIRES: int = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES: int = timedelta(days=7)
    # 图片验证码配置
    CAPTCHA_LEN: int = 4
    CAPTCHA_TTL: int = 300
    # 静态资源目录
    # STATIC_DIR: str = os.path.join(os.getcwd(), "static/")
    # TEMPLATE_DIR: str = os.path.join(os.getcwd(), "tamplates/")
    # 安全密钥, 用于session会话
    SECRET_KEY: ClassVar[str] = "session"
    SESSION_COOKIE: str = "session_id"
    SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
    WTF_CSRF_ENABLED: bool = True
    # 跨域请求
    CORS_RESOURCES: List = ["*"]
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # MySQL数据库
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root"
    MYSQL_PORT: int = 3306
    MYSQL_DBNAME: str = "flaskx"
    SQLALCHEMY_DATABASE_URI: str = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DBNAME}"
    )
    # Redis数据库
    REDIS_URL = "redis://:root@localhost:6379/0"
    # API文档密钥
    # SIWA_USER: str = "admin"
    # SIWA_PASSWORD: str = "admin"
    SIWA_UI: str = "rapidoc"
    APIKEY: str = "apikey"
    # 邮箱配置
    # smtp邮箱配置
    MAIL_SERVER: str = "smtp.qq.com"
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USE_TLS: bool = False
    MAIL_USERNAME = "2095672353@qq.com"
    MAIL_PASSWORD = "lvxzgcuntqereeeg"
    MAIL_DEFAULT_SENDER: str = "2095672353@qq.com"
    # resend邮箱配置
    RESEND_API_KEY: str = "re_KQpi5oP9_8MpwWFezjHTcFzrJhwE4F9Gj"
    RESEND_SENDER: str = "no-reply@no-reply.zwntl.cn"


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
