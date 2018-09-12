from app import app
from flask import jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
import models
import views
import resources

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
# jwt config
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

models.db.init_app(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    models.db.create_all()


@app.route('/')
def index():
    return jsonify({'message': 'hello world!'})


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    '''
    check black token
    '''
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8118)
