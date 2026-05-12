import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Titanic dataset
data = sns.load_dataset('titanic')

# Display dataset info
print(data.head())
print(data.info())
print(data.describe())

# Check missing values
print(data.isnull().sum())

# Fill missing Age values
data['age'] = data['age'].fillna(np.mean(data['age']))

# Box Plot
sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=data,
    palette='Set2'
)

plt.title('Distribution of Age with respect to Gender and Survival')

plt.show()

#pip install pandas numpy matplotlib seaborn
