# app/config.py
import os

class Config:
    DEBUG = os.getenv('FLASK_ENV') == 'development'
    MODEL_PATH = os.getenv('MODEL_PATH', 'trained_models/best_model_pipeline.joblib')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Utilise la variable d'environnement
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
