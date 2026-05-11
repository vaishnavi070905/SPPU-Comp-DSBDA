
import pandas as pd

# Load dataset
df = pd.read_csv("student_data.csv")

# Mean
print("Mean:\n", df.groupby('Department')['Marks'].mean())

# Median
print("\nMedian:\n", df.groupby('Department')['Marks'].median())

# Minimum
print("\nMinimum:\n", df.groupby('Department')['Marks'].min())

# Maximum
print("\nMaximum:\n", df.groupby('Department')['Marks'].max())

# Standard Deviation
print("\nStandard Deviation:\n", df.groupby('Department')['Marks'].std())

