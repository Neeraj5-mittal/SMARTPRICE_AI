import joblib

model = joblib.load(
    "models/house_price_model.pkl"
)

columns = joblib.load(
    "models/model_columns.pkl"
)