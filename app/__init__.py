# third-party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local 
from config import app_config

# database
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app,db) # db ve model'leri eşitler. flask db init  -  flask db migrate - flask db upgrade

    from app import models

    from .controller.home import home
    app.register_blueprint(home)

    

    return app