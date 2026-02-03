import pandas as pd
import os
import numpy as np
import re

# Paths
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")

INPUT_FILE = os.path.join(DATA_FOLDER, "phonebook.csv")
OUTPUT_FILE = os.path.join(DATA_FOLDER, "phonebook_cleaned.csv")


def clean_dataset():
    print("📥 Loading dataset...")
    df = pd.read_csv(INPUT_FILE)

    print("\n--- ORIGINAL DATA SAMPLE ---")
    print(df.head(20))

    # -------------------------------
    # 1. Remove duplicate rows
    # -------------------------------
    df = df.drop_duplicates()

    # -------------------------------
    # 2. Fill missing Names
    # -------------------------------
    df["Name"] = df["Name"].fillna("Unknown")
    df["Name"] = df["Name"].replace("", "Unknown")

    # -------------------------------
    # 3. Fix wrong datatypes
    # -------------------------------
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Percentage"] = pd.to_numeric(df["Percentage"], errors="coerce")

    # -------------------------------
    # 4. Fix Outliers (using mean)
    # -------------------------------
    # Age outliers (valid range 5–100)
    age_mean = df[(df["Age"] >= 5) & (df["Age"] <= 100)]["Age"].mean()
    df.loc[(df["Age"] < 5) | (df["Age"] > 100), "Age"] = age_mean

    # Percentage outliers (0–100)
    per_mean = df[(df["Percentage"] >= 0) & (df["Percentage"] <= 100)]["Percentage"].mean()
    df.loc[(df["Percentage"] < 0) | (df["Percentage"] > 100), "Percentage"] = per_mean

    # Fill NaN numeric values with mean
    df["Age"] = df["Age"].fillna(age_mean)
    df["Percentage"] = df["Percentage"].fillna(per_mean)

    # -------------------------------
    # 5. Fix Invalid Class Values
    # -------------------------------
    valid_classes = ["SY-AIML", "SY-DS", "SY-CS"]
    df["Class"] = df["Class"].where(df["Class"].isin(valid_classes), "Unknown")

    # -------------------------------
    # 6. Validate Phone Numbers (DO NOT CHANGE)
    # -------------------------------
    def check_phone(phone):
        phone = str(phone)
        if re.fullmatch(r"\d{10}", phone):
            return phone
        else:
            return phone  # Just keep but mark invalid separately

    df["Phone"] = df["Phone"].apply(check_phone)

    # -------------------------------
    # Save cleaned dataset to NEW FILE
    # -------------------------------
    df.to_csv(OUTPUT_FILE, index=False)

    print("\n✅ CLEANED DATA SAVED TO:")
    print(OUTPUT_FILE)
    print("\n--- CLEANED DATA SAMPLE ---")
    print(df.head(20))
