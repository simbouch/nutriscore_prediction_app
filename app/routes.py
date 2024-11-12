# app/routes.py

from flask import Blueprint, render_template, jsonify, request
import pandas as pd
from .models import db, Prediction, load_model_pipeline

api = Blueprint('api', __name__)

# Load the saved model pipeline
model_pipeline = load_model_pipeline()

@api.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@api.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json
        df = pd.DataFrame([input_data])
        prediction = model_pipeline.predict(df)[0]

        prediction_mapping = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 
            'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'
        }
        prediction_grade = prediction_mapping.get(prediction, prediction)

        # Save prediction to the database
        new_prediction = Prediction(
            pnns_groups_1=input_data.get('pnns_groups_1'),
            pnns_groups_2=input_data.get('pnns_groups_2'),
            energy_kcal_100g=input_data.get('energy-kcal_100g'),
            fat_100g=input_data.get('fat_100g'),
            saturated_fat_100g=input_data.get('saturated-fat_100g'),
            carbohydrates_100g=input_data.get('carbohydrates_100g'),
            sugars_100g=input_data.get('sugars_100g'),
            fiber_100g=input_data.get('fiber_100g'),
            proteins_100g=input_data.get('proteins_100g'),
            salt_100g=input_data.get('salt_100g'),
            fruits_vegetables_nuts_estimate=input_data.get('fruits-vegetables-nuts-estimate-from-ingredients_100g'),
            prediction=prediction_grade
        )
        db.session.add(new_prediction)
        db.session.commit()

        return jsonify({"prediction": prediction_grade, "id": new_prediction.id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
