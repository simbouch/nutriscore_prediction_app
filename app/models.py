# models.py
from config import Config
import joblib

def load_model_pipeline():
    """Load the trained model pipeline from the specified path."""
    return joblib.load(Config.MODEL_PATH)
