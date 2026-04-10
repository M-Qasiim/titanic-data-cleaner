## ⭐ If you found this helpful, consider starring the repo!

# Titanic Data Cleaner 🧹

A beginner-friendly Python script that automatically cleans messy CSV data.

## What it does

- Detects missing values  
- Fills numeric columns (e.g., Age) with the mean value  
- Fills text columns (e.g., Cabin, Embarked) with "Unknown"  
- Removes duplicate rows  
- Saves a cleaned CSV file  

## Dataset

Uses the famous Titanic dataset (891 passengers, 12 columns)

- 177 missing Age values  
- 687 missing Cabin values (77%)  

## How to run

```bash
pip install pandas
python data_cleaner.py
