# -*- coding: utf-8 -*-
# @Date    : 2018-09-13 00:33:22
# @Author  : Moe (bogerv@163.com)
# @Version : 1.0.0

from flask import Flask
from .admin import admin
from .user import user


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # import config module
    # register blueprint
    app.register_blueprint(admin)
    app.register_blueprint(user)
    return app
