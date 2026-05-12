import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Boston Housing Dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"

df = pd.read_csv(url)

# Display First 5 Rows
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Dataset Information
print("\nDataset Info:")
df.info()

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Independent Variables (Features)
X = df.drop("medv", axis=1)

# Dependent Variable (Target)
y = df["medv"]

# Split Dataset into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Linear Regression Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predict House Prices
y_pred = model.predict(X_test)

# Display Actual vs Predicted Values
comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\nActual vs Predicted House Prices:")
print(comparison.head(10))

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

# Display Evaluation Metrics
print("\nModel Evaluation:")

print("Mean Squared Error (MSE):", mse)

print("Root Mean Squared Error (RMSE):", rmse)

print("R2 Score:", r2)

# Display Coefficients with Feature Names
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients:")
print(coef_df)

# Display Intercept
print("\nIntercept:")
print(model.intercept_)

print("\nLinear Regression Model Completed Successfully")

#pip install pandas numpy scikit-learn

