from flask import Blueprint, jsonify, render_template, request, redirect, url_for, current_app
import pandas as pd

# Define a Blueprint for the main routes
main = Blueprint("main", __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route("/nutriscore_form", methods=['POST'])
def nutriscore_form():
    '''
    Predict the nutriscore grade based on the nutrients data submited in the form

    return: a jsonified message with the predicted grade
    '''
    try:
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
        model = current_app.model
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
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        return redirect(url_for("main.index"))
