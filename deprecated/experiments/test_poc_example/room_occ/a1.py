import pandas as pd

data = pd.read_csv('training_data.csv')
print(data.head())

# Summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Visualize the distribution of Room_Occupancy_Count
import seaborn as sns
sns.histplot(data['Room_Occupancy_Count'])

from sklearn.model_selection import train_test_split

# Separate target variable
X = data.drop(columns=['Room_Occupancy_Count', 'Date', 'Time'])
y = data['Room_Occupancy_Count']

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

# Define models
rf_model = RandomForestClassifier(random_state=42)
gb_model = GradientBoostingClassifier(random_state=42)
svc_model = SVC(random_state=42)

# Train models
rf_model.fit(X_train_scaled, y_train)
gb_model.fit(X_train_scaled, y_train)
svc_model.fit(X_train_scaled, y_train)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

models = [rf_model, gb_model, svc_model]
model_names = ['Random Forest', 'Gradient Boosting', 'Support Vector Classifier']

for model, name in zip(models, model_names):
    y_pred = model.predict(X_val_scaled)
    print(f"{name}:")
    print("Accuracy:", accuracy_score(y_val, y_pred))
    print("Precision:", precision_score(y_val, y_pred, average='macro'))
    print("Recall:", recall_score(y_val, y_pred, average='macro'))
    print("F1 Score:", f1_score(y_val, y_pred, average='macro'))
    print("---------")

from sklearn.model_selection import GridSearchCV

# Hyperparameters to tune
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Instantiate GridSearchCV
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid,
                           cv=3, n_jobs=-1, verbose=2, scoring='accuracy')

# Fit to the data
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print("Best parameters:", best_params)

# Train the best model
best_rf_model = RandomForestClassifier(**best_params, random_state=42)
best_rf_model.fit(X_train_scaled, y_train)

# Evaluate on the validation set
y_pred_best_rf = best_rf_model.predict(X_val_scaled)
print("Accuracy:", accuracy_score(y_val, y_pred_best_rf))
print("Precision:", precision_score(y_val, y_pred_best_rf, average='macro'))
print("Recall:", recall_score(y_val, y_pred_best_rf, average='macro'))
print("F1 Score:", f1_score(y_val, y_pred_best_rf, average='macro'))
