# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
train_data = pd.read_csv('./data/titanic/train.csv')
test_data = pd.read_csv('./data/titanic/test.csv')

# Create new feature FamilySize as a combination of SibSp and Parch
for dataset in [train_data, test_data]:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

# Drop the columns which won't be used
train_data = train_data.drop(['Ticket', 'Cabin', 'Name'], axis=1)
test_data = test_data.drop(['Ticket', 'Cabin', 'Name'], axis=1)

# Handling missing data for the 'Age' column
imputer_age = SimpleImputer(strategy='median')

train_data['Age'] = imputer_age.fit_transform(train_data['Age'].values.reshape(-1, 1))
test_data['Age'] = imputer_age.transform(test_data['Age'].values.reshape(-1, 1))

# Handling missing data for the 'Fare' column
imputer_fare = SimpleImputer(strategy='median')

train_data['Fare'] = imputer_fare.fit_transform(train_data['Fare'].values.reshape(-1, 1))
test_data['Fare'] = imputer_fare.transform(test_data['Fare'].values.reshape(-1, 1))

# Handling missing categorical data for the 'Embarked' column
imputer_embarked = SimpleImputer(strategy='most_frequent')

train_data['Embarked'] = imputer_embarked.fit_transform(train_data['Embarked'].values.reshape(-1, 1))
test_data['Embarked'] = imputer_embarked.transform(test_data['Embarked'].values.reshape(-1, 1))

# Encode categorical data
encoder = OneHotEncoder()
train_encoded = encoder.fit_transform(train_data[['Sex', 'Embarked']])
test_encoded = encoder.transform(test_data[['Sex', 'Embarked']])

train_data = pd.concat([train_data, pd.DataFrame(train_encoded.toarray(), columns=encoder.get_feature_names_out(['Sex', 'Embarked']))], axis=1)
test_data = pd.concat([test_data, pd.DataFrame(test_encoded.toarray(), columns=encoder.get_feature_names_out(['Sex', 'Embarked']))], axis=1)

# Drop the original categorical columns (they are replaced by the encoded ones)
train_data = train_data.drop(['Sex', 'Embarked'], axis=1)
test_data = test_data.drop(['Sex', 'Embarked'], axis=1)

# Split training data into input and output
X = train_data.drop(['Survived'], axis=1)
y = train_data['Survived']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(random_state=1)

# Define a grid for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'criterion': ['gini', 'entropy']
}

# Use GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

# Find the best parameters from the GridSearch
best_parameters = grid_search.best_params_

print(f'Best Parameters: {best_parameters}')

# Use the best model to make predictions on the validation set and compute accuracy
best_model = grid_search.best_estimator_
val_predictions = best_model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_predictions)

print(f'Validation Accuracy: {val_accuracy}')

# Make predictions on the test data
predictions = best_model.predict(test_data)

# Create the submission dataframe
submission = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})

# Export the predictions to a CSV file
submission.to_csv('submission.csv', index=False)
