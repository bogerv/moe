from flask import Blueprint
from flask_restful import Api

web = Blueprint(
    'web',
    __name__,
    template_folder='templates',
    static_folder='static'
)


from . import views

api = Api(web)
# api.add_resource(views.AllUsers, '/users')
# api.add_resource(views.SecretResource, '/secret')
