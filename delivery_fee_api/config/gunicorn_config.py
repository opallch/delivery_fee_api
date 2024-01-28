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
