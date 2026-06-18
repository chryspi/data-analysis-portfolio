import pandas as pd

df = pd.read_csv("heart_disease_dataset.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nHeart Disease Counts:")
print(df["Heart Disease"].value_counts())
