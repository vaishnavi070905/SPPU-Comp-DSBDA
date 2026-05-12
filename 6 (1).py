import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv")

df = df.dropna()

X = df.drop('class', axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)

TP = np.diag(cm)
FP = np.sum(cm, axis=0) - TP
FN = np.sum(cm, axis=1) - TP
TN = np.sum(cm) - (FP + FN + TP)

print("Confusion Matrix:")
print(cm)

print("\nAccuracy:", accuracy)

print("\nTP:", TP)
print("FP:", FP)
print("FN:", FN)
print("TN:", TN)

precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("\nPrecision:", precision)
print("Recall:", recall)

print("\nCompleted")

#pip install pandas numpy scikit-learn

