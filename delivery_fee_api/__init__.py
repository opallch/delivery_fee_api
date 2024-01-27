from flask import Flask
from delivery_fee_api import blueprints


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(blueprints.delivery_fee_calculator)
    app.register_blueprint(blueprints.error_handler)
    
    # TODO add debug mode and logging
    return app
