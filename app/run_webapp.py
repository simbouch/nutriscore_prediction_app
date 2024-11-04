from flask import Flask, jsonify, render_template, request, redirect, url_for
from joblib import load
import pandas as pd

app = Flask(__name__) # Creating flask object
app.config['DEBUG'] = True # Launching the debugger

# Loading the trained model
model = load('./nutriscore_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/nutriscore_form", methods=['POST'])
def nutriscore_form():
    '''
    Predict the nutriscore grade based on the nutrients data submited in the form

    return: a jsonified message with the predicted grade
    '''

    # Fetching data from the form
    if request.method == 'POST':
        data = {
            'fat_100g': [float(request.form['fat_100g'])],
            'saturated-fat_100g': [float(request.form['saturated-fat_100g'])],
            'carbohydrates_100g': [float(request.form['carbohydrates_100g'])],
            'sugars_100g': [float(request.form['sugars_100g'])],
            'fiber_100g': [float(request.form['fiber_100g'])],
            'proteins_100g': [float(request.form['proteins_100g'])],
            'salt_100g': [float(request.form['salt_100g'])],
            'sodium_100g': [float(request.form['sodium_100g'])],
            'fruits-vegetables-nuts-estimate-from-ingredients_100g': [float(request.form['fvn_estimate_100g'])],
            'energy-kcal_100g': [float(request.form['energy-kcal_100g'])]
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

    # The message and nutriscore grade to show as the prediction result under the form
    response_message = f"Nutriscore: {prediction_list[0]}"

    # Returning the message as JSON
    return jsonify({'message': response_message})

if __name__ == "__main__":
    app.run(debug=True)
