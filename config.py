import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    MODEL_PATH = os.path.join("nutriscore_model.joblib")