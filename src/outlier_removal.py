import pandas as pd
import numpy as np

df = pd.read_csv(
    "datasets/house/processed_house_data.csv"
)

print("Before Outlier Removal:")
print(df.shape)

# --------------------------------------------------
# Remove houses with less than 300 sqft per BHK
# --------------------------------------------------

df = df[
    ~(df["total_sqft"] / df["bhk"] < 300)
]

print("\nAfter BHK Outlier Removal:")
print(df.shape)

# --------------------------------------------------
# Remove price_per_sqft outliers
# Using Mean ± Std for each location
# --------------------------------------------------

def remove_pps_outliers(df):
    df_out = pd.DataFrame()

    for key, subdf in df.groupby("location"):

        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)

        reduced_df = subdf[
            (subdf.price_per_sqft > (m - st))
            &
            (subdf.price_per_sqft <= (m + st))
        ]

        df_out = pd.concat(
            [df_out, reduced_df],
            ignore_index=True
        )

    return df_out


df = remove_pps_outliers(df)

print("\nAfter Price Per Sqft Outlier Removal:")
print(df.shape)

# --------------------------------------------------
# Save Dataset
# --------------------------------------------------

df.to_csv(
    "datasets/house/final_house_data.csv",
    index=False
)

print("\nSaved Successfully!")