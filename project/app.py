"""
This is the root of the main package of our Flask app: project
"""

import os
import logging
from flask import Flask
from project.controllers.auth import bpAuth as auth
from project.database import db
from flasgger import Swagger

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Configure our Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://entropy:entropy123@localhost:5432/entropy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configure Swagger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "",
                "route": "/",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger",
    }


    swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Prometheus",
        "description": "Documentation",
        "contact": {
            "responsibleDeveloper": "Brayan Espinoza",
        },
        "version": "2.0.0",
    },
    "host": "localhost:5000",
    "basePath": "/",
    "securityDefinitions": {
        "bearerAuth": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "schemes": ["http", "https"],
    }

    swagger = Swagger(app, config=swagger_config, template=swagger_template)

    db.init_app(app)

    return app
