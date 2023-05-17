"""
This is the root of the main package of our Flask app: project
"""

import os
import logging
from flask import Flask
from project.controllers.auth import bpAuth as auth
from project.database import db

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    # Configure our Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://entropy:entropy123@localhost:5432/entropy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app
