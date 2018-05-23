from app import create_app
from app.user import user
from app.main import main

app = create_app()
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(main, url_prefix='/')


if __name__ == '__main__':
    app.run()
