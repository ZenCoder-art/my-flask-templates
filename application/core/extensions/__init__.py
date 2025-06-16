from application.core.extensions.cors import cors
from application.core.extensions.db import db
from application.core.extensions.jwt import jwt
from application.core.extensions.mail import mail
from application.core.extensions.migrate import migrate
from application.core.extensions.redis import redis
from application.core.extensions.resend import resend
from application.core.extensions.siwadoc import init_siwa

__all__ = ["cors", "db", "jwt", "mail", "migrate", "redis", "resend", "init_siwa"]
