from . import db

class Prediction(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True)
    pnns_groups_1 = db.Column(db.String(50))
    pnns_groups_2 = db.Column(db.String(50))
    energy_kcal_100g = db.Column(db.Float)
    fat_100g = db.Column(db.Float)
    saturated_fat_100g = db.Column(db.Float)
    carbohydrates_100g = db.Column(db.Float)
    sugars_100g = db.Column(db.Float)
    fiber_100g = db.Column(db.Float)
    proteins_100g = db.Column(db.Float)
    salt_100g = db.Column(db.Float)
    fruits_vegetables_nuts_estimate = db.Column(db.Float)
    prediction = db.Column(db.String(1))

def load_model_pipeline():
    import joblib
    return joblib.load("trained_models/best_model_pipeline.joblib")
