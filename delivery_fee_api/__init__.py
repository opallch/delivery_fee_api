from flask import Flask
from delivery_fee_api import blueprints


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(blueprints.delivery_fee_calculator)
    
    # TODO add debug mode and logging
    return app