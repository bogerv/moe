# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import ProductionConfig

db = SQLAlchemy()
moment = Moment()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    # app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
