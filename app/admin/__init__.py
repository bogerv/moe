# -*- coding: utf-8 -*-
# @Date    : 2018-09-13 00:33:01
# @Author  : Moe (bogerv@163.com)
# @Version : 1.0.0

from flask import Blueprint
from flask_restful import Api

admin = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static'
)


from . import views

api = Api(admin, prefix='/admin')
api.add_resource(views.AllUsers, '/users')
api.add_resource(views.SecretResource, '/secret')
