import pandas as pd

# Load dataset
file_path = "Titanic-Dataset.csv"
data = pd.read_csv(file_path)

print("Original Data:")
print(data.head())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing values (numeric with mean)
numeric_cols = data.select_dtypes(include=['number']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean().round(0).astype(int))

# Fill missing values (text with 'Unknown')
text_cols = data.select_dtypes(include=['object']).columns
data[text_cols] = data[text_cols].fillna("Unknown")

# Remove duplicate rows
data = data.drop_duplicates()

# Save cleaned data
cleaned_file = "cleaned_titanic-dataset.csv"
data.to_csv(cleaned_file, index=False)

print("\nData cleaned and saved successfully!")
print(f"Saved file: {cleaned_file}")

print("\nCleaned Data Preview:")
print(data.head())