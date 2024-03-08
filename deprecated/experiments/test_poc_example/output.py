import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')

# Fill missing values in Age column with the median of the ages
train["Age"].fillna(train["Age"].median(), inplace=True)
test["Age"].fillna(test["Age"].median(), inplace=True)

# Convert Sex to a binary variable
train["Sex"] = train["Sex"].apply(lambda sex: 1 if sex == "male" else 0)
test["Sex"] = test["Sex"].apply(lambda sex: 1 if sex == "male" else 0)

X = train[["Pclass", "Sex", "Age", "SibSp", "Parch"]]
y = train["Survived"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the validation set
y_val_pred = model.predict(X_val)

# Evaluate the model
print("Validation accuracy: ", accuracy_score(y_val, y_val_pred))

# Preprocess the test data
X_test = test[["Pclass", "Sex", "Age", "SibSp", "Parch"]]

# Make predictions on the test data
predictions = model.predict(X_test)

submission = pd.DataFrame({"PassengerId": test["PassengerId"], "Survived": predictions})

# Write the DataFrame to a csv file
submission.to_csv("submission.csv", index=False)
