# ==========================================================
# DATA WRANGLING I - TITANIC DATASET
# ==========================================================

# Import Required Libraries
import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Load Titanic Dataset from Online Source
# ----------------------------------------------------------

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print("\nDataset Loaded Successfully\n")

# ----------------------------------------------------------
# Display First 5 Rows
# ----------------------------------------------------------

print("First 5 Rows of Dataset:")
print(df.head())

# ----------------------------------------------------------
# Dataset Dimensions
# ----------------------------------------------------------

print("\nShape of Dataset:")
print(df.shape)

# ----------------------------------------------------------
# Dataset Information
# ----------------------------------------------------------

print("\nDataset Info:")
df.info()

# ----------------------------------------------------------
# Data Types of Variables
# ----------------------------------------------------------

print("\nData Types:")
print(df.dtypes)

# ----------------------------------------------------------
# Check Missing Values
# ----------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------------------------------
# Handle Missing Values
# ----------------------------------------------------------

# Fill missing Age values using Mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Embarked values using Mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Fill missing Cabin values using Mode
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# ----------------------------------------------------------
# Statistical Summary
# ----------------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# ----------------------------------------------------------
# Data Type Conversion
# ----------------------------------------------------------

# Convert Age to float
df['Age'] = df['Age'].astype(float)

# Convert Passenger Class into Category Type
df['Pclass'] = df['Pclass'].astype('category')

print("\nData Types After Conversion:")
print(df.dtypes)

# ----------------------------------------------------------
# Data Normalization
# Min-Max Normalization on Age Column
# ----------------------------------------------------------

df['Age_Normalized'] = (
    (df['Age'] - df['Age'].min()) /
    (df['Age'].max() - df['Age'].min())
)

print("\nNormalized Age Column Added")

# ----------------------------------------------------------
# Convert Categorical Variables into Numerical Variables
# ----------------------------------------------------------

# Convert Sex Column
df['Sex'] = df['Sex'].map({
    'male': 0,
    'female': 1
})

# One-Hot Encoding for Embarked Column
df = pd.get_dummies(df, columns=['Embarked'])

print("\nCategorical Variables Converted Successfully")

# ----------------------------------------------------------
# Final Dataset
# ----------------------------------------------------------

print("\nFinal Dataset (First 5 Rows):")
print(df.head())

print("\nData Wrangling I Completed Successfully")
# pip install pandas numpy