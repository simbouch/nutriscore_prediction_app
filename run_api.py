from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

# Initialize Flask app
api = Flask(__name__)
api.config['DEBUG'] = True

# Loading the trained model
model = load('./nutriscore_model.joblib')

@api.route("/predict", methods=['POST'])
def predict():
    '''
    Predict the nutriscore grade based on the nutrients data posted on Postman

    return: a jsonified list containing only the predicted grade
    '''

    # Fetching data from Postman
    data = {
        'fat_100g': [request.args.get('fat_100g', 0, type=float)],
        'saturated-fat_100g': [request.args.get('saturated-fat_100g', 0, type=float)],
        'carbohydrates_100g': [request.args.get('carbohydrates_100g', 0, type=float)],
        'sugars_100g': [request.args.get('sugars_100g', 0, type=float)],
        'fiber_100g': [request.args.get('fiber_100g', 0, type=float)],
        'proteins_100g': [request.args.get('proteins_100g', 0, type=float)],
        'salt_100g': [request.args.get('salt_100g', 0, type=float)],
        'sodium_100g': [request.args.get('sodium_100g', 0, type=float)],
        'fruits-vegetables-nuts-estimate-from-ingredients_100g': [request.args.get('fruits-vegetables-nuts-estimate-from-ingredients_100g', 0, type=float)],
        'energy-kcal_100g': [request.args.get('energy-kcal_100g', 0, type=float)]
    }
    # Creating a data frame based on the fetched data
    df = pd.DataFrame(data)

    # Normalizing data
    # Simply dividing by 100 works well, while using MinMaxScaler() results in prediction bias
    for column in df.columns:
        df[column] = df[column] / 100

    # Predicting the nutriscore grade
    prediction = model.predict(df)
    prediction_list = prediction.tolist() # Converting the result as a list

    # De-encoding of the nutriscore grade (otherwise, numbers are displayed instead of letters)
    match prediction_list[0]:
        case 1:
            prediction_list[0] = 'a'
        case 2:
            prediction_list[0] = 'b'
        case 3:
            prediction_list[0] = 'c'
        case 4:
            prediction_list[0] = 'd'
        case 5:
            prediction_list[0] = 'e'

    return jsonify({'prediction': prediction_list})

if __name__ == "__main__":
    api.run(debug=True)
