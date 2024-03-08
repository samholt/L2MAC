import pandas as pd
import numpy as np
import re
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler

# Load the data
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')

# New feature FamilySize
train["FamilySize"] = train["SibSp"] + train["Parch"]
test["FamilySize"] = test["SibSp"] + test["Parch"]

# New feature Title
train["Title"] = train["Name"].apply(lambda name: name.split(',')[1].split('.')[0].strip())
test["Title"] = test["Name"].apply(lambda name: name.split(',')[1].split('.')[0].strip())

# Fill missing Embarked values with most common value
train["Embarked"].fillna(train["Embarked"].mode()[0], inplace=True)
test["Embarked"].fillna(test["Embarked"].mode()[0], inplace=True)

# Convert Sex to a binary variable
train["Sex"] = train["Sex"].apply(lambda sex: 1 if sex == "male" else 0)
test["Sex"] = test["Sex"].apply(lambda sex: 1 if sex == "male" else 0)

# Prepare data for modeling
X = train.drop(["Survived", "Name", "Ticket", "Cabin"], axis=1)
y = train["Survived"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipelines for both numeric and categorical data.
numeric_features = ['Age', 'Fare', 'FamilySize']
numeric_transformer = Pipeline(steps=[
    ('imputer', KNNImputer(n_neighbors=2)),
    ('scaler', StandardScaler())])

categorical_features = ['Embarked', 'Sex', 'Pclass', 'Title']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Append classifier to preprocessing pipeline.
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42))])

# Tune model hyperparameters using GridSearchCV
param_grid = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__learning_rate': [0.1, 0.01, 0.001],
    'classifier__max_depth': [3, 4, 5]
}

grid_search = GridSearchCV(clf, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Evaluate the model
y_val_pred = grid_search.predict(X_val)
print("Validation accuracy: ", accuracy_score(y_val, y_val_pred))

# Use the model with the best hyperparameters to make predictions on the test data
X_test = test.drop(["Name", "Ticket", "Cabin"], axis=1)
predictions = grid_search.predict(X_test)

# Create the submission file
submission = pd.DataFrame({"PassengerId": test["PassengerId"], "Survived": predictions})
submission.to_csv("submission.csv", index=False)
