# debug config
DEBUG = True

# sql config
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'some-secret-string'

# jwt config
JWT_SECRET_KEY = 'jwt-secret-string'
JWT_SECRET_KEY = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
