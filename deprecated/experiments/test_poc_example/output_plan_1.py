import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load the datasets
train_data = pd.read_csv('./data/titanic/train.csv')
test_data = pd.read_csv('./data/titanic/test.csv')

# Handling missing values
train_data.isnull().sum()
test_data.isnull().sum()

# Strategy for imputation
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
train_data['Name'] = label_encoder.fit_transform(train_data['Name'])

# Drop irrelevant columns
train_data.drop(['PassengerId', 'Ticket', 'Cabin'], axis=1, inplace=True)


# Encoding categorical variables
encoder = LabelEncoder()
encoder.fit(train_data['Sex'])  # Fit encoder on training data
train_data['Sex'] = encoder.transform(train_data['Sex'])
test_data['Sex'] = encoder.transform(test_data['Sex'])  # Use the same encoder on test data

encoder.fit(train_data['Embarked'])  # Fit encoder on training data
train_data['Embarked'] = encoder.transform(train_data['Embarked'])
test_data['Embarked'] = encoder.transform(test_data['Embarked'])  # Use the same encoder on test data

# Normalizing numerical features
scaler = MinMaxScaler()
train_data[['Age', 'Fare']] = scaler.fit_transform(train_data[['Age', 'Fare']])
test_data[['Age', 'Fare']] = scaler.transform(test_data[['Age', 'Fare']])

# Splitting the train data into a training and validation set
X = train_data.drop('Survived', axis=1)
y = train_data['Survived']
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Verify the shapes of the split datasets
print("\nTraining Data - X_train:")
print("Shape:", X_train.shape)

print("\nValidation Data - X_valid:")
print("Shape:", X_valid.shape)

print("\nTraining Data - y_train:")
print("Shape:", y_train.shape)

print("\nValidation Data - y_valid:")
print("Shape:", y_valid.shape)

# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import GridSearchCV

# # Define the hyperparameters to tune
# parameters = {
#     'n_estimators': [100, 200, 300],
#     'learning_rate': [0.1, 0.01, 0.001],
#     'max_depth': [3, 5, 7]
# }

# # Create the gradient boosting classifier
# gb = GradientBoostingClassifier()

# # Perform grid search to find the best hyperparameters
# gb_cv = GridSearchCV(gb, parameters, cv=5)
# gb_cv.fit(X, y)

# # Get the best hyperparameters
# best_gb = gb_cv.best_estimator_

# # Print the best hyperparameters
# print("Best Hyperparameters for Gradient Boosting: ", best_gb)

from sklearn.ensemble import GradientBoostingClassifier

# Create the GradientBoostingClassifier with the best hyperparameters
best_gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, max_depth=5)

# Train the model
best_gb.fit(X, y)

# Make predictions on the test data
predictions = best_gb.predict(X)

