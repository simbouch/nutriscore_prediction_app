from flask import Flask

def create_app():
    # Initialising flask object
    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Load configuration settings
    app.config.from_object('config.Config')

    # Register routes
    with app.app_context():
        from . import routes

    return app
