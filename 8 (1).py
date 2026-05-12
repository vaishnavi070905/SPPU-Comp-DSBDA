import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
data = sns.load_dataset('titanic')

# First 5 rows
print(data.head())

# Dataset information
print(data.info())

# Check missing values
print(data.isnull().sum())

# -------------------------------
# Count Plot - Survival Count
# -------------------------------
sns.countplot(x='survived', data=data)
plt.title("Survival Count")
plt.show()

# -------------------------------
# Count Plot - Passenger Class
# -------------------------------
sns.countplot(x='pclass', data=data)
plt.title("Passenger Class Count")
plt.show()

# -------------------------------
# Count Plot - Gender
# -------------------------------
sns.countplot(x='sex', data=data)
plt.title("Gender Count")
plt.show()

# -------------------------------
# Histogram of Fare
# -------------------------------
plt.hist(data['fare'].dropna(), bins=30)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.show()

#pip install pandas numpy matplotlib seaborn
