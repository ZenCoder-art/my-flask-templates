from core.extensions.cors import CORSExtension
from core.extensions.csrf import CSRFExtension
from core.extensions.db import DBSessionExtension
from core.extensions.jwt import JWTManagerExtension
from core.extensions.mail import MailExtension
from core.extensions.migrate import MigrateExtension
from core.extensions.redis import RedisExtension
from core.extensions.resend import ResendExtension
from core.extensions.api import APIExtension

__all__ = [
    "APIExtension",
    "CORSExtension",
    "CSRFExtension",
    "DBSessionExtension",
    "JWTManagerExtension",
    "MailExtension",
    "MigrateExtension",
    "RedisExtension",
    "ResendExtension",
]
