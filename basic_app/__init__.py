from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()
try:
    import basic_app.config as config
except:
    import config

import os
db = SQLAlchemy()

def load_models():
    from basic_app.users import models
load_models()

def init_extensions(app):
    db.init_app(app)

def init_views(app):
    from basic_app  import users
    app.register_blueprint(users.bp,url_prefix="")

def is_mac():
    if "Darwin" in os.uname():
        print("mac")
        return True
    print("linux")
    return False

def create_app():
    app = Flask(__name__)
    if is_mac():
        # load config
        app.config['SQLALCHEMY_DATABASE_URI'] = config.db_path
        print(config.db_path)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    init_extensions(app)
    init_views(app)
    return app


manager = Manager(create_app)
