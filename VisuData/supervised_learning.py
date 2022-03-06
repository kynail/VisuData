import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import seaborn as sn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('train.csv')
df.head(12)
df.shape
y = df["SalePrice"]
X = df[["Id","LotArea"]]
X.head()
y.head()

test_size = 0.33
seed = 7
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=test_size, random_state=seed)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_train)
print(accuracy_score(y_train, predictions))

predictions = model.predict(X_test)

df = X_test.copy()
df['SalePrice'] = y_test
df['LotArea'] = predictions
df
