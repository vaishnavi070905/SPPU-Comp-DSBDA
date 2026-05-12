
import pandas as pd
import numpy as np

print("\nDataset Creation\n")

# Create dataset
data = {
    "Student_ID": [1,2,3,4,5,6,7,8,9,10],
    "Math": [78, 85, np.nan, 90, 120, 60, 75, 88, 95, 200],
    "Science": [80, 70, 65, np.nan, 85, 55, 60, 75, 95, 100],
    "English": [75, 65, 70, 60, 80, 55, 90, 85, np.nan, 95],
    "Attendance": [85, 90, 95, 80, 75, np.nan, 88, 92, 85, 110]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 1: Handle Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

# Step 2: Detect and Handle Outliers using IQR
print("\nOutlier Detection using IQR Method\n")

for col in ["Math", "Science", "English", "Attendance"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    print(f"{col} -> Lower Limit: {lower:.2f}, Upper Limit: {upper:.2f}")

    # Replace outliers with median
    median = df[col].median()
    df[col] = np.where((df[col] < lower) | (df[col] > upper), median, df[col])

print("\nAfter Removing Outliers:")
print(df)

# Step 3: Data Transformation
print("\nApplying Log Transformation on Math Column")

df["Math_log"] = np.log(df["Math"] + 1)

print("\nTransformed Values:")
print(df[["Math", "Math_log"]])

# Final Output
print("\nFinal Cleaned Dataset:")
print(df)

print("\nData Wrangling II Completed Successfully")

# pip install pandas numpy
