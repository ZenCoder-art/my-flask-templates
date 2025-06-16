from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

from application.core.extensions import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(30), unique=True, nullable=False, index=True)
    password = db.Column(db.String(512), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def set_password(self, password: str):
        """将明文密码加密存储"""
        self.password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        """校验输入的密码是否与存储的哈希匹配"""
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f"<User {self.username}>"
