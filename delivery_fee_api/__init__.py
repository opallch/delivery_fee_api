import logging
import pathlib
from logging.config import dictConfig
from flask import Flask
from delivery_fee_api import blueprints, constants

def create_app() -> Flask:

    app = Flask(__name__)
    app.register_blueprint(blueprints.delivery_fee_calculator)
    app.register_blueprint(blueprints.error_handler)
    
    if app.debug:
        logging.basicConfig(level=logging.DEBUG)

    return app
