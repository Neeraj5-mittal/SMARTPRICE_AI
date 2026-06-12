from fastapi import FastAPI
import pandas as pd

from backend.schemas import HouseRequest
from backend.model_loader import model, columns

app = FastAPI(
    title="SmartPrice AI",
    description="House Price Prediction API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "SmartPrice AI Running"
    }


@app.post("/predict-house")
def predict_house(data: HouseRequest):

    input_data = {
        col: 0.0 for col in columns
    }

    input_data["total_sqft"] = float(data.total_sqft)
    input_data["bath"] = float(data.bath)
    input_data["balcony"] = float(data.balcony)
    input_data["bhk"] = float(data.bhk)

    location_column = f"location_{data.location}"

    if location_column in input_data:
        input_data[location_column] = 1.0

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    predicted_price = round(float(prediction[0]), 2)

    return {
    "predicted_price_lakhs": predicted_price,
    "predicted_price_inr": int(predicted_price * 100000),
    "currency": "INR",
    "model": "House Price Predictor"
}