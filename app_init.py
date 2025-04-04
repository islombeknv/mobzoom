import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import Base

db = SQLAlchemy(model_class=Base)
app = Flask("TaskManager")
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(views, auth):
    app.register_blueprint(views.bp)
    app.register_blueprint(auth.bp)
    app.secret_key = "GTYlv>K]0=otL=B`@z^s"
    # for sqlite
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/python_web.db'
    # for postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/python_web'
    with app.app_context():
        db.init_app(app)
    return app

