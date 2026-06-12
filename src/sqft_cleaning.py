import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("datasets/house/cleaned_house_data.csv")

print("=" * 50)
print("DATASET BEFORE SQFT CLEANING")
print("=" * 50)
print("Shape:", df.shape)

# --------------------------------------------------
# Function to convert total_sqft to numeric
# --------------------------------------------------

def convert_sqft_to_num(x):
    tokens = str(x).split('-')

    # Range values like 1133 - 1384
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2

    try:
        return float(x)

    except:
        return np.nan


# Apply conversion
df["total_sqft"] = df["total_sqft"].apply(convert_sqft_to_num)

print("\nMissing Values After Conversion:")
print(df["total_sqft"].isnull().sum())

# --------------------------------------------------
# Remove rows where sqft couldn't be converted
# --------------------------------------------------

df = df.dropna(subset=["total_sqft"])

print("\nShape After Removing Invalid Sqft Rows:")
print(df.shape)

# --------------------------------------------------
# Create Price Per Sqft Feature
# --------------------------------------------------

df["price_per_sqft"] = (
    df["price"] * 100000
) / df["total_sqft"]

print("\nPrice Per Sqft Sample:")
print(
    df[
        ["price", "total_sqft", "price_per_sqft"]
    ].head()
)

# --------------------------------------------------
# Statistical Summary
# --------------------------------------------------

print("\nPrice Per Sqft Statistics:")
print(df["price_per_sqft"].describe())

# --------------------------------------------------
# Save Processed Dataset
# --------------------------------------------------

df.to_csv(
    "datasets/house/processed_house_data.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")
print("File: datasets/house/processed_house_data.csv")