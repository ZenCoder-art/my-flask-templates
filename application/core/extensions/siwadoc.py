from flask import Flask
from flask_siwadoc import SiwaDoc


def init_siwa(app: Flask):
    siwadoc = SiwaDoc(
        title=app.config["TITLE"],
        description=app.config["DESCRIPTION"],
        version=app.config["VERSION"],
        ui=app.config["SIWA_UI"],
    )
    return siwadoc
