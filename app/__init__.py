from flask import Flask
from config import Config

def create_app():
    # Initialising flask object
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config.from_object(Config)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register routes
    with app.app_context():
        from app.models import load_model
        app.model = load_model()

    return app
