import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("\nFirst 5 Rows:")
print(df.head())

df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 35, 60, 100], labels=['Child', 'Young', 'Adult', 'Senior'])

print("\nAge Group Distribution:")
print(df['Age_Group'].value_counts())

group_stats = df.groupby('Age_Group')['Fare'].agg(['mean', 'median', 'min', 'max', 'std'])

print("\nSummary Statistics of Fare grouped by Age Group:")
print(group_stats)

fare_lists = df.groupby('Age_Group')['Fare'].apply(list)

print("\nList of Fare values for each Age Group:")
print(fare_lists)

iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

print("\nFirst 5 Rows of Iris Dataset:")
print(iris.head())

iris_stats = iris.groupby('species').describe()

print("\nStatistical Details of Each Species:")
print(iris_stats)

print("\nPercentiles (Sepal Length) for Each Species:")

for species in iris['species'].unique():
    data = iris[iris['species'] == species]['sepal_length']
    print("\nSpecies:", species)
    print("Mean:", data.mean())
    print("Standard Deviation:", data.std())
    print("25th Percentile:", np.percentile(data, 25))
    print("50th Percentile:", np.percentile(data, 50))
    print("75th Percentile:", np.percentile(data, 75))

print("\nCompleted")

#pip install pandas numpy



