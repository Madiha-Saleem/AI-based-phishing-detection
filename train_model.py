import pandas as pd

# Load dataset
df = pd.read_csv("dataset/phishing.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())