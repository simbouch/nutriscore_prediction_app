### NutriScore Wizard
NutriScore Wizard is a web application that predicts the NutriScore grade for food products based on their nutritional information. The app provides an intuitive interface for users to input product details, and it returns an easy-to-understand NutriScore grade, helping users make informed dietary choices.

### Table of Contents
Project Overview
Features
Tech Stack
Installation
Usage
API Endpoints
Security Measures
File Structure
Future Improvements
Contributing
License
###  Project Overview
NutriScore Wizard is built to provide a quick and accurate NutriScore grade prediction based on a food product's nutritional data. The NutriScore system rates products from "A" (healthiest) to "E" (least healthy), helping consumers make better food choices. The project combines machine learning with a user-friendly web interface to deliver this functionality.

### Features
Input Validation: Ensures data entered by users is correctly formatted.
Real-Time NutriScore Prediction: Predicts NutriScore based on product nutritional information.
Ergonomic User Interface: Bootstrap-enhanced interface for seamless user experience.
REST API Endpoint: JSON-based API endpoint for integrating predictions into other applications.
Security Features: Implements CSRF protection, secure HTTP headers, and input sanitization.
Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS (Bootstrap), JavaScript (jQuery)
Machine Learning: Scikit-learn for training and prediction
Database: None (Data is processed in-memory for predictions)
APIs: RESTful API for NutriScore prediction
Installation
### Clone the repository:


git clone https://github.com/your-username/nutriscore-wizard.git
cd nutriscore-wizard
### Create a virtual environment and activate it:


python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Run the Flask application:


python run.py
### Access the application: Open your browser and navigate to http://127.0.0.1:5000

### Usage
Enter Nutritional Information: Use the form to input relevant product data (e.g., calories, fat, fiber, etc.).
Predict NutriScore: Click the "Get NutriScore" button to receive the prediction.
View Results: The predicted NutriScore will appear on the same page, indicating the health grade for the product.
API Endpoints
POST /predict
### Description: Provides a prediction for the NutriScore grade based on input data.

Request Format (JSON):


{
  "pnns_groups_1": "sugary snacks",
  "pnns_groups_2": "biscuits and cakes",
  "energy-kcal_100g": 456,
  "fat_100g": 12.3,
  "saturated-fat_100g": 5.2,
  "carbohydrates_100g": 65.0,
  "sugars_100g": 40.0,
  "fiber_100g": 5.0,
  "proteins_100g": 3.5,
  "salt_100g": 0.8,
  "fruits-vegetables-nuts-estimate-from-ingredients_100g": 0
}
Response Format (JSON):


{
  "prediction": "A"
}
Security Measures
CSRF Protection: Prevents cross-site request forgery on form submissions.
Input Validation: Ensures only valid data is processed for predictions.
Secure HTTP Headers: Mitigates XSS, clickjacking, and MIME sniffing risks.
HTTPS: Recommended for production deployment to secure data in transit.
###  File Structure

nutriscore_prediction_app/
├── app/
│   ├── __init__.py             # Initializes Flask app
│   ├── routes.py               # Routes for API and frontend
│   ├── models.py               # Machine learning model loading
│   ├── templates/
│   │   ├── index.html          # Main form for input
│   │   └── result.html         # Display prediction result (if used separately)
│   └── static/
│       ├── style.css           # Custom CSS
├── data/
│   └── final_csv_4.csv         # Dataset used for training
├── notebooks/                  # Jupyter notebooks for model training
├── tests/                      # Test cases for API
├── trained_models/
│   └── best_model_pipeline.joblib  # Trained model pipeline
├── venv/                       # Virtual environment
├── config.py                   # Application configuration
├── run.py                      # Runs the Flask application
└── requirements.txt            # Project dependencies
### Future Improvements
User Authentication: Add user registration and login to personalize NutriScore recommendations.
Extended Validation: Implement additional data validation techniques to handle edge cases.
History of Predictions: Allow users to view past predictions and analyze trends.
Internationalization: Add multilingual support for global accessibility.
Contributing
We welcome contributions! If you'd like to contribute, please follow these steps:

###  Fork the repository.
Create a branch for your feature (git checkout -b feature-name).
Commit your changes (git commit -m 'Add new feature').
Push to your branch (git push origin feature-name).
Open a Pull Request.
### License
This project is licensed under the MIT License. See LICENSE for more information.
