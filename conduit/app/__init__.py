import os 
from flask import Flask,jsonify,g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    """Create an application instance"""
    app = Flask(__name__)
    #applying configuration
    cfg_file_path = os.path.join(os.getcwd(),'config',config + '.py')
    app.config.from_pyfile(cfg_file_path)

    #Initialize extensions
    db.init_app(app)

    #register blueprints todo


    return app


