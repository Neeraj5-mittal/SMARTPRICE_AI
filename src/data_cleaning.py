import pandas as pd

# Load dataset
df = pd.read_csv("datasets/house/bengaluru_house_prices.csv")

print("=" * 50)
print("ORIGINAL DATASET")
print("=" * 50)
print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# Drop society column (too many missing values)
# --------------------------------------------------
df = df.drop("society", axis=1)

# --------------------------------------------------
# Remove rows with missing values
# --------------------------------------------------
df = df.dropna()

print("\n" + "=" * 50)
print("AFTER CLEANING")
print("=" * 50)
print("Shape:", df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# Extract BHK from size column
# Example:
# 2 BHK -> 2
# 4 Bedroom -> 4
# --------------------------------------------------
df["bhk"] = df["size"].apply(
    lambda x: int(str(x).split()[0])
)

print("\n" + "=" * 50)
print("BHK COLUMN CREATED")
print("=" * 50)

print(df[["size", "bhk"]].head())

# --------------------------------------------------
# Check BHK distribution
# --------------------------------------------------
print("\nTop BHK Counts:")
print(df["bhk"].value_counts().head(10))

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------
print("\nDataset Info:")
print(df.info())

# --------------------------------------------------
# Statistical Summary
# --------------------------------------------------
print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# Save cleaned dataset
# --------------------------------------------------
df.to_csv(
    "datasets/house/cleaned_house_data.csv",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")
print("📁 File: datasets/house/cleaned_house_data.csv")