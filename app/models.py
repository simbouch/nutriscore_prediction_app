import joblib
import os
from flask import current_app

def load_model():
    try:
        # Load model from the app configuration
        model_path = current_app.config.get("MODEL_PATH", "nutriscore_model.joblib")
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
