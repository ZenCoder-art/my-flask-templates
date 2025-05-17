from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_siwadoc import SiwaDoc
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
siwa = SiwaDoc(
    title="my flask template title",
    description="my flask template 符合Restful API风格",
    version="0.1.0",
    ui="swagger",
)
mail = Mail()
cors = CORS()
