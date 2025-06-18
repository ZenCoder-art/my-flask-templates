#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apps import create_application

app = create_application()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
