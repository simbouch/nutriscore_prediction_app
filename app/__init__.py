from flask import Flask
from config import Config

# Function to create and configure the app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register the Blueprint for routes
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Load the model within the app context
    with app.app_context():
        from app.models import load_model
        app.model = load_model()  # Load the model and attach it to the app instance

    return app
