import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Display Dataset Information
print(data.head())
print(data.describe())
print(data.describe(include='object'))
print(data.isnull().sum())

# Feature Types
print("\nFeatures and their types:")
print(data.dtypes)

# Histograms
sns.histplot(x=data['sepal_length'], kde=True)
plt.title("Sepal Length Distribution")
plt.show()

sns.histplot(x=data['sepal_width'], kde=True)
plt.title("Sepal Width Distribution")
plt.show()

sns.histplot(x=data['petal_length'], kde=True)
plt.title("Petal Length Distribution")
plt.show()

sns.histplot(x=data['petal_width'], kde=True)
plt.title("Petal Width Distribution")
plt.show()

# Boxplots
sns.boxplot(x=data['sepal_length'])
plt.show()

sns.boxplot(x=data['sepal_width'])
plt.show()

sns.boxplot(x=data['petal_length'])
plt.show()

sns.boxplot(x=data['petal_width'])
plt.show()

# Species Comparison
sns.boxplot(x='sepal_length', y='species', data=data)
plt.show()

sns.boxplot(x='petal_length', y='species', data=data)
plt.show()