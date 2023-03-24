from flask import Flask
from flask_migrate import Migrate

from admin import admin
# from api import init_api
# from api import init_api
from articles.views import article
from auth.views import auth_app, login_manager
from author.views import authors
from models.database import db
from security import flask_bcrypt

from user.views import user
from views import main_page

migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    app.secret_key = 'super secret key'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    login_manager.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    flask_bcrypt.init_app(app)
    # api = init_api(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(authors)
    app.register_blueprint(main_page)
    app.register_blueprint(auth_app)
