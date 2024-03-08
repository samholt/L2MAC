import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier

# Load the data
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')

# Create a title feature
train['Title'] = train['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())
test['Title'] = test['Name'].apply(lambda name: name.split(',')[1].split('.')[0].strip())

# Fill missing embarked values with mode
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
test['Embarked'].fillna(test['Embarked'].mode()[0], inplace=True)

# Convert sex to binary
train['Sex'] = train['Sex'].apply(lambda sex: 1 if sex == 'male' else 0)
test['Sex'] = test['Sex'].apply(lambda sex: 1 if sex == 'male' else 0)

# Fill missing ages with median age for each title
median_ages = train.groupby('Title')['Age'].median()
train['Age'] = train.apply(lambda row: median_ages[row['Title']] if pd.isnull(row['Age']) else row['Age'], axis=1)
test['Age'] = test.apply(lambda row: median_ages[row['Title']] if pd.isnull(row['Age']) else row['Age'], axis=1)

# Binning age and fare
train['AgeBin'] = pd.qcut(train['Age'], 4).astype(str)
test['AgeBin'] = pd.qcut(test['Age'], 4).astype(str)

train['FareBin'] = pd.qcut(train['Fare'], 4).astype(str)
test['FareBin'] = pd.qcut(test['Fare'], 4).astype(str)

# New Features
train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1

train['IsAlone'] = train['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
test['IsAlone'] = test['FamilySize'].apply(lambda x: 1 if x == 1 else 0)

# Preparing the data for modeling
X = train.drop(['Survived', 'Name', 'Ticket', 'Cabin', 'Age', 'Fare'], axis=1)
y = train['Survived']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipelines for both numeric and categorical data.
numeric_features = ['SibSp', 'Parch', 'FamilySize', 'IsAlone']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())])

categorical_features = ['Pclass', 'Sex', 'Embarked', 'Title', 'AgeBin', 'FareBin']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Define the base models
level0 = list()
level0.append(('lr', LogisticRegression()))
level0.append(('rf', RandomForestClassifier()))
level0.append(('svm', SVC()))

# Define meta learner model
level1 = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Define the stacking ensemble
model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)

# Append classifier to preprocessing pipeline.
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', model)])

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'classifier__final_estimator__learning_rate': [0.1, 0.01, 0.001],
    'classifier__final_estimator__n_estimators': [50, 100, 200],
    'classifier__final_estimator__max_depth': [3, 5, 7]
}

grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Evaluate the model
y_val_pred = grid_search.predict(X_val)
print("Validation accuracy: ", accuracy_score(y_val, y_val_pred))

# Use the model to make predictions on the test data
X_test = test.drop(['Name', 'Ticket', 'Cabin', 'Age', 'Fare'], axis=1)
predictions = grid_search.predict(X_test)

# Create the submission file
submission = pd.DataFrame({'PassengerId': test['PassengerId'], 'Survived': predictions})
submission.to_csv('submission.csv', index=False)
