# models.py
import joblib

def load_model_pipeline():
    """Load the trained model pipeline from the specified path."""
    model_path = "C:/data/simplon_dev_ia_projects/flask_projects/nutriscore_prediction_app/trained_models/best_model_pipeline.joblib"
    return joblib.load(model_path)
