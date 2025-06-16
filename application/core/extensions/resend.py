import resend


def init_resend(app):
    resend.api_key = app.config["RESEND_API_KEY"]
