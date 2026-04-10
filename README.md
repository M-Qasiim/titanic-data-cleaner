# Titanic Data Cleaner 🧹

A Python script that automatically cleans messy CSV data.

## What it does
- Detects missing values
- Fills numeric columns (Age) with rounded mean
- Fills text columns (Cabin, Embarked) with "Unknown"
- Removes duplicate rows
- Saves a cleaned CSV file

## Dataset
Uses the famous Titanic dataset (891 passengers, 12 columns)
- 177 missing Age values
- 687 missing Cabin values (77%!)

## How to run
pip install pandas
python data_cleaner.py

## Before & After
| Column   | Missing Before | After   |
|----------|---------------|---------|
| Age      | 177           | 0       |
| Cabin    | 687           | 0       |
| Embarked | 2             | 0       |

## ⭐ If you found this helpful, consider starring the repo!
