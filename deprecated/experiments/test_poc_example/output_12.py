import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from scipy.stats import skew, norm
from scipy.special import boxcox1p

# Load the data
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')

# Store PassengerId for submission
PassengerId = test['PassengerId']

# Create new features
train['FamilySize'] = train['SibSp'] + train['Parch'] + 1
train['IsAlone'] = 1 #initialize to yes/1 is alone
train['IsAlone'].loc[train['FamilySize'] > 1] = 0 # now update to no/0 if family size is greater than 1

# Apply same changes to test data
test['FamilySize'] = test['SibSp'] + test['Parch'] + 1
test['IsAlone'] = 1
test['IsAlone'].loc[test['FamilySize'] > 1] = 0

# Complete missing fare with median
train['Fare'].fillna(train['Fare'].median(), inplace = True)
test['Fare'].fillna(test['Fare'].median(), inplace = True)

# Apply log to Fare to reduce skewness distribution
train["Fare"] = train["Fare"].map(lambda i: np.log(i) if i > 0 else 0)
test["Fare"] = test["Fare"].map(lambda i: np.log(i) if i > 0 else 0)

# Fill Embarked nan values of dataset set with 'S' most frequent value
train["Embarked"] = train["Embarked"].fillna("S")
test["Embarked"] = test["Embarked"].fillna("S")

# Complete missing age with median
train['Age'].fillna(train['Age'].median(), inplace = True)
test['Age'].fillna(test['Age'].median(), inplace = True)

# Creating a categorical variable for Age and Fare
train['AgeBin'] = pd.qcut(train['Age'], 4)
train['FareBin'] = pd.qcut(train['Fare'], 4)

test['AgeBin'] = pd.qcut(test['Age'], 4)
test['FareBin'] = pd.qcut(test['Fare'], 4)

# Dropping irrelevant features
drop_elements = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'SibSp']
train = train.drop(drop_elements, axis = 1)
test  = test.drop(drop_elements, axis = 1)

# Classifier Comparison
logreg = LogisticRegression()
svc = SVC(probability=True)
rf = RandomForestClassifier()

# Ensemble Modeling
votingC = VotingClassifier(estimators=[('rf', rf), ('logreg', logreg), ('svc', svc)], voting='soft')

# Preparing the data for modeling
X = train.drop(['Survived'], axis=1)
y = train['Survived']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipelines for both numeric and categorical data.
numeric_features = ['Parch', 'FamilySize']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())])

categorical_features = ['Pclass', 'Sex', 'Embarked', 'IsAlone', 'AgeBin', 'FareBin']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Append classifier to preprocessing pipeline.
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', votingC)])

clf.fit(X_train, y_train)

# Predict the validation set results
y_val_pred = clf.predict(X_val)

# Print accuracy
print("Validation accuracy: ", accuracy_score(y_val, y_val_pred))

# Use the model to make predictions on the test data
predictions = clf.predict(test)

# Create the submission file
submission = pd.DataFrame({'PassengerId': PassengerId, 'Survived': predictions})
submission.to_csv('submission.csv', index=False)
