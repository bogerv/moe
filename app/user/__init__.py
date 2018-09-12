from flask import Blueprint
from flask_restful import Api


user = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static'
)


from . import views

api = Api(user, prefix='/user')

api.add_resource(views.UserRegistration, '/registration')
api.add_resource(views.UserLogin, '/login')
api.add_resource(views.UserLogoutAccess, '/logout/access')
api.add_resource(views.UserLogoutRefresh, '/logout/refresh')
api.add_resource(views.TokenRefresh, '/token/refresh')
