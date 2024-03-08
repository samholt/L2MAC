import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

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

# Binning age and fare
train['AgeBin'] = pd.qcut(train['Age'], 4).astype(str)
test['AgeBin'] = pd.qcut(test['Age'], 4).astype(str)

train['FareBin'] = pd.qcut(train['Fare'], 4).astype(str)
test['FareBin'] = pd.qcut(test['Fare'], 4).astype(str)

# Preparing the data for modeling
X = train.drop(['Survived', 'Name', 'Ticket', 'Cabin', 'Age', 'Fare'], axis=1)
y = train['Survived']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipelines for both numeric and categorical data.
numeric_features = ['SibSp', 'Parch']
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

# Create an ensemble model
model1 = LogisticRegression(random_state=1)
model2 = RandomForestClassifier(random_state=1)
model3 = SVC(probability=True)

model = VotingClassifier(estimators=[('lr', model1), ('rf', model2), ('svc', model3)], voting='soft')

# Append classifier to preprocessing pipeline.
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', model)])

clf.fit(X_train, y_train)

# Evaluate the model
y_val_pred = clf.predict(X_val)
print("Validation accuracy: ", accuracy_score(y_val, y_val_pred))

# Use the model with the best hyperparameters to make predictions on the test data
X_test = test.drop(['Name', 'Ticket', 'Cabin', 'Age', 'Fare'], axis=1)
predictions = clf.predict(X_test)

# Create the submission file
submission = pd.DataFrame({'PassengerId': test['PassengerId'], 'Survived': predictions})
submission.to_csv('submission.csv', index=False)
