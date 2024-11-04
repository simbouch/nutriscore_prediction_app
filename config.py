import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    MODEL_PATH = os.path.join("trained_models", "best_model.joblib")
