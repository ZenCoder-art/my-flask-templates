from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class LoginSchema(BaseModel):
    username: str = Field(
        ..., min_length=3, max_length=32, example="admin", description="用户名或者邮箱"
    )
    password: str = Field(
        ..., min_length=6, max_length=128, example="123456", description="用户密码"
    )


class RegisterSchema(BaseModel):
    username: str = Field(
        ..., min_length=3, max_length=32, description="用户名", example="admin"
    )
    email: EmailStr = Field(..., description="邮箱地址", example="2095672353@qq.com")
    password: str = Field(
        ..., min_length=6, max_length=128, description="密码", example="123456"
    )


class TokenSchema(BaseModel):
    Authorization: str = Field(..., example="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...")


class UserResetSchema(BaseModel):
    old_password: str = Field(
        ...,
        min_length=6,
        max_length=128,
        example="123456",
        description="用户的初始密码",
    )
    new_password: str = Field(
        ...,
        min_length=6,
        max_length=128,
        example="123456789",
        description="用户需要修改的密码",
    )


class EmailSchema(BaseModel):
    email: EmailStr = Field(
        ..., description="接收验证码的邮箱地址", example="3391164183@qq.com"
    )
    method: Literal["smtp", "resend"] = Field(
        default="smtp", example="smtp", description="可选值为smtp和resend"
    )
    subject: str = Field(
        default="您的验证码", description="邮件主题", example="您的验证码"
    )
    sender: str = Field(default="Me", description="发件人昵称", example="测试")


class EmailVerifySchema(BaseModel):
    email: EmailStr = Field(..., description="邮箱地址", example="3391164183@qq.com")
    code: str = Field(..., description="验证码")


class CaptchaVerifySchema(BaseModel):
    captcha_id: str = Field(
        ...,
        min_length=6,
        max_length=64,
        description="验证码对应的唯一 ID（由后端生成并返回）",
    )
    code: str = Field(
        ..., min_length=3, max_length=10, description="用户输入的图片验证码"
    )
