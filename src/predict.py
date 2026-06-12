import pandas as pd
import joblib

# Load model
model = joblib.load("models/house_price_model.pkl")

# Load columns
columns = joblib.load("models/model_columns.pkl")

# Create input dictionary
input_data = dict.fromkeys(columns, 0)

# Example House
input_data["total_sqft"] = 1200
input_data["bath"] = 2
input_data["balcony"] = 1
input_data["bhk"] = 2

# Example location
location = "Whitefield"

location_column = f"location_{location}"

if location_column in input_data:
    input_data[location_column] = 1

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict
prediction = model.predict(input_df)

print(f"\nPredicted House Price: ₹{prediction[0]:.2f} Lakhs")