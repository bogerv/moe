# -*- coding: utf-8 -*-
# @Date    : 2018-09-13 00:34:49
# @Author  : Moe (bogerv@163.com)
# @Version : 1.0.0

from app import create_app
from flask import jsonify
from flask_jwt_extended import JWTManager
from models import db, RevokedTokenModel


app = create_app()

db.init_app(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return jsonify({'message': 'hello world!'})


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    '''
    check black token
    '''
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8118)
