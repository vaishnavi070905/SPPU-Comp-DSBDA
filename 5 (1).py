import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load Social Network Ads dataset from direct CSV link
df = pd.read_csv("https://raw.githubusercontent.com/shivang98/Social-Network-ads-Boost/refs/heads/master/Social_Network_Ads.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Features and target variable
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Feature Scaling
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Logistic Regression Model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

# Predict test results
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

# Performance Metrics
accuracy = (TP + TN) / (TP + TN + FP + FN)

error_rate = (FP + FN) / (TP + TN + FP + FN)

precision = TP / (TP + FP) if (TP + FP) != 0 else 0

recall = TP / (TP + FN) if (TP + FN) != 0 else 0

# Output Results
print("\nConfusion Matrix:")
print(cm)

print("\nTP:", TP)
print("FP:", FP)
print("TN:", TN)
print("FN:", FN)

print("\nAccuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)

print("\nCompleted")

#pip install pandas numpy scikit-learn

