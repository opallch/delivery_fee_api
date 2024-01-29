import logging
from logging.config import dictConfig
from flask import Flask
from delivery_fee_api import blueprints, constants

def config_logging(app:Flask):
    dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            },
            "http_request": {
                "format": "[%(asctime)s] [HTTP %(method)s] payload=%(payload)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z"
            },
            "http_response": {
                "format": "[%(asctime)s] [HTTP RESPONSE] payload=%(payload)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z"
            },
            "http_error": {
                "format": "[%(asctime)s] [HTTP ERROR | %(code)s %(error_name)s]\n%(description)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "console_http_error": {
                "class": "logging.StreamHandler",
                "formatter": "http_error",
            },
            "file_http_request": {
                "class": "logging.FileHandler",
                "filename": "delivery_fee_api_http.log",
                "formatter": "http_request",
            },
            "file_http_response": {
                "class": "logging.FileHandler",
                "filename": "delivery_fee_api_http.log",
                "formatter": "http_response",
            },
            "file_http_error": {
                "class": "logging.FileHandler",
                "filename": "delivery_fee_api_http.log",
                "formatter": "http_error",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
        "loggers": {
            "delivery_fee_api.blueprints.delivery_fee_calculator.request": {
                "level": "INFO",
                "handlers": ["file_http_request"],
                "propagate": False,
            },
            "delivery_fee_api.blueprints.delivery_fee_calculator.response": {
                "level": "INFO",
                "handlers": ["file_http_response"],
                "propagate": False,
            },
            "delivery_fee_api.blueprints.error_handler": {
                "level": "ERROR",
                "handlers": ["console_http_error", "file_http_error"],
                "propagate": False,
            }
        }
        }
    )

    if app.debug:
        logging.basicConfig(level=logging.DEBUG)

def create_app() -> Flask:

    app = Flask(__name__)
    app.register_blueprint(blueprints.delivery_fee_calculator)
    app.register_blueprint(blueprints.error_handler)
    
    config_logging(app)
    return app
