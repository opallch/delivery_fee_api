"""
Configuration for gunicorn which must be passed on startup
`via --config python:delivery_fee_api.config.gunicorn_config`.
References:
https://docs.gunicorn.org/en/latest/settings.html
https://github.com/benoitc/gunicorn/blob/master/gunicorn/config.py.
"""

from delivery_fee_api import constants

workers = 4
bind = f'0.0.0.0:{constants.FLASK_PORT}'
pidfile = 'delivery_fee_api.pid'
timeout = 300

logconfig_dict = {
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
                "filename": constants.LOG_PATH / "delivery_fee_api_http.log",
                "formatter": "http_request",
            },
            "file_http_response": {
                "class": "logging.FileHandler",
                "filename": constants.LOG_PATH / "delivery_fee_api_http.log",
                "formatter": "http_response",
            },
            "file_http_error": {
                "class": "logging.FileHandler",
                "filename": str(constants.LOG_PATH / "delivery_fee_api_http.log"),
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
