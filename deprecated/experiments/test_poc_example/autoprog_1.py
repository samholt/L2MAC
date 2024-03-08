import pandas as pd
from pathlib import Path

from autoprognosis.studies.classifiers import ClassifierStudy
from autoprognosis.utils.serialization import load_model_from_file
from autoprognosis.utils.tester import evaluate_estimator

# Load datasets
train_df = pd.read_csv('./data/titanic/train.csv')
test_df = pd.read_csv('./data/titanic/test.csv')

# Preprocessing: Fill missing values, drop unnecessary columns etc. Here we are assuming 'Age' and 'Fare' columns have missing values and filling them with their mean.
train_df['Age'].fillna((train_df['Age'].mean()), inplace=True)
test_df['Age'].fillna((test_df['Age'].mean()), inplace=True)
train_df['Fare'].fillna((train_df['Fare'].mean()), inplace=True)
test_df['Fare'].fillna((test_df['Fare'].mean()), inplace=True)

# Convert categorical data to numeric. Here we assume 'Sex' and 'Embarked' are categorical columns
train_df = pd.get_dummies(train_df, columns=['Sex', 'Embarked'])
test_df = pd.get_dummies(test_df, columns=['Sex', 'Embarked'])

# Drop unnecessary columns
columns_to_drop = ['Name', 'Ticket', 'Cabin']
train_df.drop(columns=columns_to_drop, inplace=True)
test_df.drop(columns=columns_to_drop, inplace=True)

# Assign target and drop it from training dataset
Y = train_df['Survived']
train_df.drop(['Survived'], axis=1, inplace=True)
X = train_df

workspace = Path("workspace")
study_name = "titanic_study"

study = ClassifierStudy(
    study_name=study_name,
    dataset=pd.concat([X, Y], axis=1),  # pandas DataFrame
    target="Survived",  # the label column in the dataset
    num_iter=100,  # how many trials to do for each candidate
    timeout=60,  # seconds
    classifiers=["logistic_regression", "random_forest"],
    workspace=workspace,
)

study.run()

output = workspace / study_name / "model.p"
model = load_model_from_file(output)

# Evaluate the model
metrics = evaluate_estimator(model, X, Y)

print(f"model {model.name()} -> {metrics['str']}")

# Train the model
model.fit(X, Y)

# Now use the model to predict the 'Survived' outcome in the test data
predictions = model.predict(test_df)

# Generate a submission dataframe
submission = pd.DataFrame({
    "PassengerId": test_df["PassengerId"],
    "Survived": predictions
})

# Write submission to CSV
submission.to_csv('submission.csv', index=False)
