# __init__.py
from flask import Flask
from .routes import api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprint
    app.register_blueprint(api)

    return app
