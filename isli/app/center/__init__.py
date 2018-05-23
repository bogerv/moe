# coding: utf-8

from flask import Blueprint

center = Blueprint('center', __name__)

from . import views
