import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from xgboost import XGBRegressor

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv(
    "datasets/house/final_house_data.csv"
)

print("=" * 50)
print("DATASET LOADED")
print("=" * 50)
print("Shape:", df.shape)

# ==================================================
# KEEP REQUIRED COLUMNS
# ==================================================

df = df[
    [
        "location",
        "total_sqft",
        "bath",
        "balcony",
        "bhk",
        "price"
    ]
]

# ==================================================
# REDUCE RARE LOCATIONS
# ==================================================

location_stats = df["location"].value_counts()

location_stats_less_than_10 = (
    location_stats[location_stats <= 10]
)

df["location"] = df["location"].apply(
    lambda x: "other"
    if x in location_stats_less_than_10
    else x
)

print("\nUnique Locations After Reduction:")
print(df["location"].nunique())

# ==================================================
# ONE HOT ENCODING
# ==================================================

df = pd.get_dummies(
    df,
    columns=["location"],
    drop_first=True
)

# Convert bool → int
for col in df.columns:
    if df[col].dtype == "bool":
        df[col] = df[col].astype(int)

# ==================================================
# FEATURES & TARGET
# ==================================================

X = df.drop("price", axis=1)
y = df["price"]

# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==================================================
# LINEAR REGRESSION
# ==================================================

print("\n" + "=" * 50)
print("LINEAR REGRESSION")
print("=" * 50)

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_r2 = r2_score(y_test, lr_pred)
lr_mae = mean_absolute_error(y_test, lr_pred)
lr_rmse = mean_squared_error(y_test, lr_pred) ** 0.5

print("R2 Score :", round(lr_r2, 4))
print("MAE      :", round(lr_mae, 4))
print("RMSE     :", round(lr_rmse, 4))

# ==================================================
# RANDOM FOREST
# ==================================================

print("\n" + "=" * 50)
print("RANDOM FOREST")
print("=" * 50)

rf_model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = mean_squared_error(y_test, rf_pred) ** 0.5

print("R2 Score :", round(rf_r2, 4))
print("MAE      :", round(rf_mae, 4))
print("RMSE     :", round(rf_rmse, 4))

# ==================================================
# XGBOOST
# ==================================================

print("\n" + "=" * 50)
print("XGBOOST")
print("=" * 50)

xgb_model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)

xgb_r2 = r2_score(y_test, xgb_pred)
xgb_mae = mean_absolute_error(y_test, xgb_pred)
xgb_rmse = mean_squared_error(y_test, xgb_pred) ** 0.5

print("R2 Score :", round(xgb_r2, 4))
print("MAE      :", round(xgb_mae, 4))
print("RMSE     :", round(xgb_rmse, 4))

# ==================================================
# SELECT BEST MODEL
# ==================================================

scores = {
    "Linear Regression": lr_r2,
    "Random Forest": rf_r2,
    "XGBoost": xgb_r2
}

best_name = max(scores, key=lambda k: scores[k])

if best_name == "Linear Regression":
    best_model = lr_model

elif best_name == "Random Forest":
    best_model = rf_model

else:
    best_model = xgb_model

# ==================================================
# SAVE MODEL
# ==================================================

joblib.dump(
    best_model,
    "models/house_price_model.pkl"
)

joblib.dump(
    X.columns.tolist(),
    "models/model_columns.pkl"
)

print("\n" + "=" * 50)
print("BEST MODEL")
print("=" * 50)

print("Selected:", best_name)
print("Best R2 :", round(scores[best_name], 4))

print("\nModel Saved:")
print("models/house_price_model.pkl")

print("\nColumns Saved:")
print("models/model_columns.pkl")