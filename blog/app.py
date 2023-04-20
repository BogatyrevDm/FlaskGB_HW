from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, redirect, url_for
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')
    app.config['SECRET_KEY'] = 'j^2$8xli&%fnf(+imu&7b$i53gv14%()@^3t$f%gt+orj4=+*h'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.article.views import article
    from blog.user.views import user
    from blog.auth.views import auth
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
