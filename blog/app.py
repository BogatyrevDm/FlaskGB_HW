from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from blog.article.views import article
from blog.user.views import user
from blog.auth.views import auth

db = SQLAlchemy()
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')
    app.config['SECRET_KEY'] = 'j^2$8xli&%fnf(+imu&7b$i53gv14%()@^3t$f%gt+orj4=+*h'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    from .models import User

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)


