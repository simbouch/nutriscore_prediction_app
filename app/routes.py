from flask import Blueprint, render_template, jsonify, request
import pandas as pd
from .models import load_model_pipeline

# Blueprint for API and main routes
api = Blueprint('api', __name__)

# Load the saved model pipeline
model_pipeline = load_model_pipeline()

# Route to render the main index page
@api.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Prediction route
@api.route("/predict", methods=["POST"])
def predict():
    """API endpoint to predict Nutri-Score grade based on input features."""
    try:
        # Collect and parse input data from JSON
        input_data = request.json
        
        # Convert to DataFrame to match model input format
        df = pd.DataFrame([input_data])
        
        # Make prediction using the model pipeline
        prediction = model_pipeline.predict(df)[0]
        
        # Extended prediction mapping to handle lowercase predictions
        prediction_mapping = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 
            'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'
        }
        prediction_grade = prediction_mapping.get(prediction, prediction)

        # Return prediction result as JSON
        return jsonify({"prediction": prediction_grade})

    except Exception as e:
        # Log any errors encountered during prediction
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500
