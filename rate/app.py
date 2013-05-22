from flask import Flask

from .api import api
from .frontend import frontend


def configure_app(app):
    app.config.from_object('rate.settings')

    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix='/api')


def create_app():
    app = Flask(__name__)
    configure_app(app)
    return app
