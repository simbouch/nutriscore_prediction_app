import joblib
import os
from flask import current_app

def load_model():
    try:
        # Load model path from the app configuration
        model_path = current_app.config.get("MODEL_PATH", "trained_models/best_model_1.joblib")
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
