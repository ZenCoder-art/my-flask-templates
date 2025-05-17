#!/usr/bin/env python3

import sys

from gunicorn.app.wsgiapp import WSGIApplication


def run():
    sys.argv = [
        "gunicorn",
        "application:application",
        "--bind",
        "0.0.0.0:9000",
        "--workers",
        "4",
        "--log-level",
        "info",
        "--access-logfile",
        "-",
        "--error-logfile",
        "-",
        "--access-logfile",
        "./logs/access.log",
        "--error-logfile",
        "./logs/error.log",
    ]
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()


if __name__ == "__main__":
    run()
