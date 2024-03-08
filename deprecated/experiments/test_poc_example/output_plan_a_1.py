import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import seaborn as sns
import re

# Load datasets
train = pd.read_csv('./data/titanic/train.csv')
test = pd.read_csv('./data/titanic/test.csv')

# Identify missing values in the datasets
print("Missing values in train dataset:")
print(train.isnull().sum())
print("\nMissing values in test dataset:")
print(test.isnull().sum())

# Strategies to handle these missing values:
# For 'Age', 'Fare' - we can fill the missing values with the median of the column
# For 'Embarked', 'Cabin' - we can fill the missing values with the most frequent value in the column

# Creating the SimpleImputer object instances
age_imputer = SimpleImputer(strategy='median')
fare_imputer = SimpleImputer(strategy='median')
embarked_imputer = SimpleImputer(strategy='most_frequent')
cabin_imputer = SimpleImputer(strategy='most_frequent')

# Applying the imputation on 'Age', 'Embarked', 'Cabin', 'Fare' columns
train['Age'] = age_imputer.fit_transform(train['Age'].values.reshape(-1, 1))
test['Age'] = age_imputer.transform(test['Age'].values.reshape(-1, 1))

train['Embarked'] = embarked_imputer.fit_transform(train['Embarked'].values.reshape(-1, 1))
test['Embarked'] = embarked_imputer.transform(test['Embarked'].values.reshape(-1, 1))

train['Cabin'] = cabin_imputer.fit_transform(train['Cabin'].values.reshape(-1, 1))
test['Cabin'] = cabin_imputer.transform(test['Cabin'].values.reshape(-1, 1))

test['Fare'] = fare_imputer.fit_transform(test['Fare'].values.reshape(-1, 1))

# Encoding categorical variables using OneHotEncoder
encoder = OneHotEncoder(drop='first')  # drop one category to avoid "dummy variable trap"

train_encoded = pd.get_dummies(train, columns=["Sex", "Embarked"], drop_first=True)
test_encoded = pd.get_dummies(test, columns=["Sex", "Embarked"], drop_first=True)

# Perform feature scaling on the dataset
scaler = StandardScaler()

# Selecting the numerical features to scale
features_to_scale = ['Age', 'Fare']

# Scaling 'Age' and 'Fare' in both train and test datasets
train_encoded[features_to_scale] = scaler.fit_transform(train_encoded[features_to_scale])
test_encoded[features_to_scale] = scaler.transform(test_encoded[features_to_scale])

import matplotlib.pyplot as plt

# Correlation Matrix Heatmap
corr = train_encoded.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Matrix')
plt.show()

# Barplot of survival by sex
sns.barplot(x="Sex_male", y="Survived", data=train_encoded)
plt.title('Survival by Sex')
plt.show()

# Barplot of survival by Passenger Class
sns.barplot(x="Pclass", y="Survived", data=train_encoded)
plt.title('Survival by Passenger Class')
plt.show()

# Histogram of Age
sns.histplot(data=train_encoded, x="Age", hue="Survived", element="step", stat="density", common_norm=False)
plt.title('Age distribution split by Survival')
plt.show()

# Boxplot of Fare paid
sns.boxplot(y='Fare',x='Survived',data=train_encoded)
plt.title('Box plot of Fare split by Survival')
plt.show()

# Pointplot of Age by Fare and Survival
sns.pointplot(x="Age", y="Fare", hue="Survived", data=train_encoded)
plt.title('Point plot of Age and Fare split by Survival')
plt.show()

# Feature Engineering - 'FamilySize' and 'IsAlone'
for dataset in [train_encoded, test_encoded]:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1

# Feature Engineering - 'Title'
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # If the title exists, extract and return it.
    if title_search:
        return title_search.group(1)
    return ""

for dataset in [train_encoded, test_encoded]:
    dataset['Title'] = dataset['Name'].apply(get_title)
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

# Encoding 'Title' using OneHotEncoder
train_encoded = pd.get_dummies(train_encoded, columns=["Title"], drop_first=True)
test_encoded = pd.get_dummies(test_encoded, columns=["Title"], drop_first=True)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Define feature matrix X and the target y
X = train_encoded.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y = train_encoded['Survived']

# Split the dataset into a training set and a validation set
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the models
random_forest = RandomForestClassifier(n_estimators=100)
svc = SVC(gamma='auto')
logistic_regression = LogisticRegression(solver='liblinear')

# Train the models
random_forest.fit(X_train, y_train)
svc.fit(X_train, y_train)
logistic_regression.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Predict on the validation set
y_pred_rf = random_forest.predict(X_val)
y_pred_svc = svc.predict(X_val)
y_pred_lr = logistic_regression.predict(X_val)

# Evaluation - Accuracy, Precision, Recall, F1-Score
models = ['Random Forest', 'SVC', 'Logistic Regression']
predictions = [y_pred_rf, y_pred_svc, y_pred_lr]

for i, model in enumerate(models):
    print(f"{model} Model: ")
    print(f"Accuracy: {accuracy_score(y_val, predictions[i])}")
    print(f"Precision: {precision_score(y_val, predictions[i])}")
    print(f"Recall: {recall_score(y_val, predictions[i])}")
    print(f"F1-Score: {f1_score(y_val, predictions[i])}")
    print(f"Confusion Matrix: \n{confusion_matrix(y_val, predictions[i])}\n")

# Select the model with highest accuracy as the best model
accuracies = [accuracy_score(y_val, y_pred_rf), accuracy_score(y_val, y_pred_svc), accuracy_score(y_val, y_pred_lr)]
best_model_index = accuracies.index(max(accuracies))
best_model = models[best_model_index]
print(f"The best model based on Accuracy is: {best_model}")

from sklearn.model_selection import GridSearchCV

# Define the parameter grid for RandomForest
param_grid = {
    'n_estimators': [100, 200, 300, 500],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize the grid search model
grid_search = GridSearchCV(estimator=random_forest, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print(f"Best parameters: {best_params}")

# Re-train the model with the best parameters
best_rf = RandomForestClassifier(**best_params)
best_rf.fit(X_train, y_train)

# Predict on the validation set
y_pred_best_rf = best_rf.predict(X_val)

# Evaluation - Accuracy, Precision, Recall, F1-Score
print(f"Optimized Random Forest Model: ")
print(f"Accuracy: {accuracy_score(y_val, y_pred_best_rf)}")
print(f"Precision: {precision_score(y_val, y_pred_best_rf)}")
print(f"Recall: {recall_score(y_val, y_pred_best_rf)}")
print(f"F1-Score: {f1_score(y_val, y_pred_best_rf)}")
print(f"Confusion Matrix: \n{confusion_matrix(y_val, y_pred_best_rf)}\n")

# Define feature matrix X and the target y for the entire training dataset
X_full = train_encoded.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y_full = train_encoded['Survived']

# Train the best model on the full training dataset
best_rf_full = RandomForestClassifier(**best_params)
best_rf_full.fit(X_full, y_full)

# Make predictions on the test dataset
test_features = test_encoded.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
predictions = best_rf_full.predict(test_features)

# Create a DataFrame for the submission
submission = pd.DataFrame({
    "PassengerId": test_encoded['PassengerId'],
    "Survived": predictions
})

# Save the submission DataFrame as a CSV file
submission.to_csv('submission.csv', index=False)

# Import required libraries
from sklearn.metrics import roc_auc_score, plot_roc_curve
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

# Evaluate the models using ROC-AUC score
models_list = [random_forest, svc, logistic_regression]
for i, model in enumerate(models_list):
    y_pred_proba = model.predict_proba(X_val)[:, 1]
    roc_auc = roc_auc_score(y_val, y_pred_proba)
    print(f"{models[i]} Model ROC-AUC Score: {roc_auc}")

# Plot ROC Curve
plt.figure(figsize=(10,8))
for i, model in enumerate(models_list):
    plot_roc_curve(model, X_val, y_val, ax=plt.gca(), name=models[i])
plt.title('Receiver Operating Characteristic Curve')
plt.show()

# Function to plot learning curve
def plot_learning_curve(estimator, title, X, y, axes=None, cv=None, n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes, return_times=True)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    # Plot learning curve
    plt.grid()
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    plt.legend(loc="best")

    return plt

# Plot learning curves
for i, model in enumerate(models_list):
    plot_learning_curve(model, models[i], X, y, cv=3)
    plt.title(f"Learning curve for {models[i]}")
    plt.show()

# Check feature importance in the random forest model
feature_importance = pd.Series(random_forest.feature_importances_, index=X.columns)
feature_importance.nlargest(10).plot(kind='barh')
plt.title('Top 10 important features in Random Forest model')
plt.show()

