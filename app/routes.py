from flask import Blueprint, render_template, request, redirect, url_for, current_app

# Define a Blueprint for the main routes
main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    """Render the homepage with the input form."""
    return render_template("index.html")

@main.route("/predict", methods=["POST"])
def predict():
    """Handle the form submission, perform prediction, and display the result."""
    try:
        # Collect form data
        categorical_data = [
            request.form.get("categories"),
            request.form.get("pnns_groups_1"),
            request.form.get("pnns_groups_2"),
            request.form.get("food_groups")
        ]
        numerical_data = [
            float(request.form.get("energy-kcal_100g", 0)),
            float(request.form.get("fat_100g", 0)),
            float(request.form.get("saturated-fat_100g", 0)),
            float(request.form.get("carbohydrates_100g", 0)),
            float(request.form.get("sugars_100g", 0)),
            float(request.form.get("fiber_100g", 0)),
            float(request.form.get("proteins_100g", 0)),
            float(request.form.get("salt_100g", 0)),
            float(request.form.get("fruits-vegetables-nuts-estimate-from-ingredients_100g", 0))
        ]

        # Combine all data for prediction
        data = categorical_data + numerical_data
        print("Form data received:", data)  # Debugging print statement

        # Access the model from the current app context
        model = current_app.model
        prediction = model.predict([data])[0]  # Perform prediction

        print("Prediction result:", prediction)  # Debugging print statement

        # Render the result page with the prediction
        return render_template("result.html", prediction=prediction)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return redirect(url_for("main.index"))
