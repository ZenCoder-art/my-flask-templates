import random
import string
from datetime import datetime

import resend
from flask import render_template
from flask_mail import Message

from core.extensions import mail


def random_number(length: int = 6):
    return "".join(random.choices("0123456789", k=length))


def random_string(length: int = 6):
    letters = string.ascii_letters
    return "".join(random.choices(letters, k=length))


def random_char(length: int = 6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def resend_send_verification_email(
    to_email: str,
    code: str,
    subject: str,
    sender: str,
    from_email: str = "no-reply@no-reply.zwntl.cn",
):
    html_content = render_template("code.html", code=code, year=datetime.now().year)
    response = resend.Emails.send(
        {
            "from": f"{sender} <{from_email}>",
            "to": [to_email],
            "subject": subject,
            "html": html_content,
        }
    )
    return response


def smtp_send_verification_email(
    to_email: str,
    code: str,
    subject: str,
    sender: str,
    from_email: str = "no-reply@no-reply.zwntl.cn",
):
    html_content = render_template("code.html", code=code, year=datetime.now().year)
    msg = Message(
        subject=subject,
        sender=(sender, from_email),
        recipients=[to_email],
        html=html_content,
    )
    mail.send(msg)
