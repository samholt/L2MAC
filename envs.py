"""
This file defines the base class for an environment and a specific data-science environment.
"""
from sklearn.metrics import accuracy_score
import pandas as pd
import importlib.util
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import importlib
import sys
import random
import numpy as np
import openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import importlib
import random
import numpy as np
from sklearn.exceptions import NotFittedError
import time
from timeout_decorator import timeout
import sys
import io
from executor import Executor
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.metrics import f1_score 
import json

# def robust_accuracy(y_true, y_pred):
#     """
#     Compute the accuracy score in a robust manner, ensuring that the data types
#     of y_true and y_pred match.
    
#     :param y_true: Ground truth labels.
#     :param y_pred: Predicted labels.
#     :return: Accuracy score.
#     """
    
#     # If y_true and y_pred are both numeric or both string, compute accuracy directly
#     if (np.issubdtype(type(y_true.iloc[0]), np.number) and np.issubdtype(type(y_pred[0]), np.number)) or \
#        (isinstance(y_true.iloc[0], str) and isinstance(y_pred[0], str)):
#         return accuracy_score(y_true, y_pred)
    
#     # If y_true is string and y_pred is numeric, encode y_true
#     if isinstance(y_true.iloc[0], str) and np.issubdtype(type(y_pred[0]), np.number):
#         le = LabelEncoder()
#         y_true_encoded = le.fit_transform(y_true)
#         return accuracy_score(y_true_encoded, y_pred)
    
#     # If y_pred is string and y_true is numeric, encode y_pred
#     if isinstance(y_pred[0], str) and np.issubdtype(type(y_true.iloc[0]), np.number):
#         le = LabelEncoder()
#         y_pred_encoded = le.fit_transform(y_pred)
#         return accuracy_score(y_true, y_pred_encoded)
    
#     # In other cases, raise a TypeError
#     raise TypeError(f"Unsupported data types: y_true type: {type(y_true.iloc[0])}, y_pred type: {type(y_pred[0])}")

def maybe_fit_preprocessor(preprocessor, X_train):
    # Attempt to transform a single record to see if preprocessor has been fitted
    try:
        preprocessor.transform(X_train.iloc[:1])
    except NotFittedError:
        # If it's not fitted, then fit it to the training data
        preprocessor.fit(X_train)

class Environment:
    def __init__(self, config, logger, env_name, seed):
        self.config = config
        self.logger = logger
        self.env_name = env_name
        self.seed = seed

    def log(self, message):
        if self.logger is not None:
            self.logger.info(f"[Environment: {self.env_name}] {message}")

    def reset(self):
        pass

    def step(self, action):
        pass




class SystemDesignOopEnvironment(Environment):
    def __init__(self, config, logger, env_name, seed):
        super().__init__(config, logger, env_name, seed)
        self.seed_value = None
        self.description = None
        self.attribute_names = None
        self.prepend_code_libraries = ''

    def set_seed(self, seed_value):
        self.seed_value = seed_value
        random.seed(seed_value)
        np.random.seed(seed_value)

    def reset(self):
        # Fetch the dataset by its OpenML ID (or by name)
        env_task_id = self.config.get('env_task_id')
        self.env_task_id = self.config.get('env_task_id')
        desc_path = f'data/donnemartin-system-design-oop/object_oriented_design/{env_task_id}/description.txt'
        with open(desc_path, 'r') as file:
            desc = file.readlines()
        ut_path = f'data/donnemartin-system-design-oop/object_oriented_design/{env_task_id}/test_all.py'
        with open(ut_path, 'r') as file:
            ut = file.readlines()
        self.desc = ''.join(desc)
        self.ut = ''.join(ut)

    def get_obs(self):
        if self.config.get('use_description', False):
            # state = f"description:{self.description}\nattribute_names:{self.attribute_names}"
            state = f"{self.attribute_names}"
            return state
        else:
            return None
        
    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_user_code_lines(self, code_string):
        # try:
        result = self.executor.execute_user_code_lines(code_string)
        # except Exception as e:
        #     print(e)
        return result
    
#     def create_baseline_prompt(self):
#         from prompts import baseline_system_prompt
#         task_prompt = f'''
# Objective: """
# {self.task_data['task_description']}
# """

# Make sure the generated code adheres to this specified code interface, as it will be unit tested against this interface: """
# {self.task_data['code_interface']}
# """
# '''
#         prompt = baseline_system_prompt(task_prompt)
#         return prompt
    
    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_final_user_code(self, code_string):
        # try:
        # Create a temporary module to hold the user code
        code_string = f'{self.prepend_code_libraries}\n{code_string}'
        user_code_module = importlib.types.ModuleType("user_code")
        exec(code_string, user_code_module.__dict__)

        # Train the model using the provided code
        self.log('Training model...')
        t0 = time.perf_counter()
        model, preprocessor = user_code_module.train_model(self.train_data.copy(), self.train_labels)
        self.log(f"Model trained. Elapsed time: {time.perf_counter() - t0}s]")
        if preprocessor is not None:
            # Preprocess the test data using the same transformer
            maybe_fit_preprocessor(preprocessor, self.train_data.copy())
            test_data_processed = preprocessor.transform(self.test_data)
            # Predict using the trained model
            try:
                predictions = model.predict(test_data_processed)
            except ValueError as e:
                predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        else:
            # Predict using the trained model
            predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        # except Exception as e:
        #     print(f"An error occurred in the user-generated code: {e}")
        #     reward = 0
        return reward

    def step(self, code_string):
        try:
            reward = self.execute_final_user_code(code_string)
        except StopIteration:
            reward = 0

        state_out = None
        done = True
        info = None
        return state_out, reward, done, info
    


class ExistingLargeCodeBaseChangeEnvironment(Environment):
    def __init__(self, config, logger, env_name, seed):
        super().__init__(config, logger, env_name, seed)
        self.seed_value = None
        self.description = None
        self.attribute_names = None
        self.prepend_code_libraries = ''

    def set_seed(self, seed_value):
        self.seed_value = seed_value
        random.seed(seed_value)
        np.random.seed(seed_value)

    def reset(self):
        # Fetch the dataset by its OpenML ID (or by name)
        env_task_id = self.config.get('env_task_id')
        self.env_task_id = self.config.get('env_task_id')
        desc_path = f'data/insight-large-code-base/{env_task_id}/description.txt'
        with open(desc_path, 'r') as file:
            desc = file.readlines()
        existing_code_path = f'data/insight-large-code-base/{env_task_id}/code_path.txt'
        with open(existing_code_path, 'r') as file:
            code_path = file.readlines()
        self.desc = ''.join(desc)
        self.code_path = ''.join(code_path)

    def get_obs(self):
        if self.config.get('use_description', False):
            # state = f"description:{self.description}\nattribute_names:{self.attribute_names}"
            state = f"{self.attribute_names}"
            return state
        else:
            return None
        
    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_user_code_lines(self, code_string):
        # try:
        result = self.executor.execute_user_code_lines(code_string)
        # except Exception as e:
        #     print(e)
        return result
    
#     def create_baseline_prompt(self):
#         from prompts import baseline_system_prompt
#         task_prompt = f'''
# Objective: """
# {self.task_data['task_description']}
# """

# Make sure the generated code adheres to this specified code interface, as it will be unit tested against this interface: """
# {self.task_data['code_interface']}
# """
# '''
#         prompt = baseline_system_prompt(task_prompt)
#         return prompt
    
    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_final_user_code(self, code_string):
        # try:
        # Create a temporary module to hold the user code
        code_string = f'{self.prepend_code_libraries}\n{code_string}'
        user_code_module = importlib.types.ModuleType("user_code")
        exec(code_string, user_code_module.__dict__)

        # Train the model using the provided code
        self.log('Training model...')
        t0 = time.perf_counter()
        model, preprocessor = user_code_module.train_model(self.train_data.copy(), self.train_labels)
        self.log(f"Model trained. Elapsed time: {time.perf_counter() - t0}s]")
        if preprocessor is not None:
            # Preprocess the test data using the same transformer
            maybe_fit_preprocessor(preprocessor, self.train_data.copy())
            test_data_processed = preprocessor.transform(self.test_data)
            # Predict using the trained model
            try:
                predictions = model.predict(test_data_processed)
            except ValueError as e:
                predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        else:
            # Predict using the trained model
            predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        # except Exception as e:
        #     print(f"An error occurred in the user-generated code: {e}")
        #     reward = 0
        return reward

    def step(self, code_string):
        try:
            reward = self.execute_final_user_code(code_string)
        except StopIteration:
            reward = 0

        state_out = None
        done = True
        info = None
        return state_out, reward, done, info
    

class DataScienceEnvironment(Environment):
    def __init__(self, config, logger, env_name):
        super().__init__(config, logger, env_name)
        self.seed_value = None
        self.description = None
        self.attribute_names = None
        self.prepend_code_libraries = 'from pandas import DataFrame, Series\nfrom sklearn.base import BaseEstimator\nfrom sklearn.compose import ColumnTransformer\nfrom typing import Tuple\nimport pandas as pd\nimport numpy as np\nfrom sklearn.preprocessing import LabelEncoder, StandardScaler\nfrom sklearn.impute import SimpleImputer\nfrom sklearn.preprocessing import OneHotEncoder'

    def set_seed(self, seed_value):
        self.seed_value = seed_value
        random.seed(seed_value)
        np.random.seed(seed_value)

    def reset(self):
        # Fetch the dataset by its OpenML ID (or by name)
        dataset_id = self.config.get('dataset_id')
        dataset_name = self.config.get('dataset_name')

        if dataset_id:
            d = openml.datasets.get_dataset(dataset_id)
        elif dataset_name:
            d = openml.datasets.get_dataset(openml.datasets.list_datasets().get(dataset_name))
        else:
            raise ValueError("Either 'dataset_id' or 'dataset_name' must be specified in the config.")

        X, y, _, attribute_names = d.get_data(target=d.default_target_attribute)
        # Convert y to numerical values if it's categorical
        if isinstance(y[0], str) or isinstance(y[0], object):  # Checking if the first element is a string or object type. You can add more conditions if needed
            encoder = LabelEncoder()
            y = encoder.fit_transform(y)
        self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(X, y, test_size=0.2, random_state=self.seed_value)

        self.description = d.description
        self.attribute_names = attribute_names

        self.executor =  Executor(variables={'X_train': self.train_data.copy(), 'y_train': self.train_labels.copy()}, prepend_code_libraries=self.prepend_code_libraries)

        return self.train_data, self.train_labels, attribute_names

    def get_obs(self):
        if self.config.get('use_description', False):
            # state = f"description:{self.description}\nattribute_names:{self.attribute_names}"
            state = f"{self.attribute_names}"
            return state
        else:
            return None
        
    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_user_code_lines(self, code_string):
        # try:
        result = self.executor.execute_user_code_lines(code_string)
        # except Exception as e:
        #     print(e)
        return result


        # # Redirect stdout to capture the output
        # old_stdout = sys.stdout
        # new_stdout = io.StringIO()
        # sys.stdout = new_stdout

        # # Execute the code
        # code_string = self.prepend_code_libraries + code_string
        # user_code_module = importlib.types.ModuleType("user_code")
        # user_code_module.__dict__['X_train'] = self.train_data.copy()
        # user_code_module.__dict__['y_train'] = self.train_labels.copy()
        # exec(code_string, user_code_module.__dict__)

        # # Reset stdout
        # sys.stdout = old_stdout
        
        # # Return the captured output
        # result = new_stdout.getvalue()
        # new_stdout.close()

        # return result
        

    # @timeout(60*3, timeout_exception=StopIteration)
    def execute_final_user_code(self, code_string):
        # try:
        # Create a temporary module to hold the user code
        code_string = f'{self.prepend_code_libraries}\n{code_string}'
        user_code_module = importlib.types.ModuleType("user_code")
        exec(code_string, user_code_module.__dict__)

        # Train the model using the provided code
        self.log('Training model...')
        t0 = time.perf_counter()
        model, preprocessor = user_code_module.train_model(self.train_data.copy(), self.train_labels)
        self.log(f"Model trained. Elapsed time: {time.perf_counter() - t0}s]")
        if preprocessor is not None:
            # Preprocess the test data using the same transformer
            maybe_fit_preprocessor(preprocessor, self.train_data.copy())
            test_data_processed = preprocessor.transform(self.test_data)
            # Predict using the trained model
            try:
                predictions = model.predict(test_data_processed)
            except ValueError as e:
                predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        else:
            # Predict using the trained model
            predictions = model.predict(self.test_data)
            # Calculate the reward as the accuracy of the prediction
            reward = f1_score(self.test_labels, predictions, average='macro')
        # except Exception as e:
        #     print(f"An error occurred in the user-generated code: {e}")
        #     reward = 0
        return reward

    def step(self, code_string):
        try:
            reward = self.execute_final_user_code(code_string)
        except StopIteration:
            reward = 0

        state_out = None
        done = True
        info = None
        return state_out, reward, done, info

def get_env(env_name, config, logger, seed):
    if 'data-science' in env_name:
        config['dataset_id'] = env_name.split('data-science')[-1][1:]
        config['use_description'] = config.setup.data_science_env_use_description
        return DataScienceEnvironment(config, logger, env_name)
    elif 'donnemartin-system-design-oop-' in env_name:
        config['env_task_id'] = env_name.split('donnemartin-system-design-oop-')[1]
        return SystemDesignOopEnvironment(config, logger, env_name, seed)
    elif 'insight-large-code-base-' in env_name:
        config['env_task_id'] = env_name.split('insight-large-code-base-')[1]
        return ExistingLargeCodeBaseChangeEnvironment(config, logger, env_name, seed)
    else:
        raise Exception(f'Environment {env_name} not found')
    
import unittest

class TestEnvironment(unittest.TestCase):
    def test_environment_iris(self):
        config = {'dataset_id': 'iris'}
        env = DataScienceEnvironment(config, None, 'data-science-iris')
        env.seed(42)
        env.reset()

        user_code_string = r"""
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model, None"""
        state_out, reward, done, info = env.step(user_code_string)
        expected_accuracy = 1.0 # Set this to an expected value for your specific dataset and model
        self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed


    def test_environment_credit_g(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string = r'''
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def train_model(X_train: DataFrame, y_train: Series) -> Tuple[BaseEstimator, ColumnTransformer]:
    """
    This function trains a logistic regression model on the given training data. The input features are preprocessed
    by applying standard scaling to numeric columns and one-hot encoding to categorical columns.

    :param X_train: A DataFrame containing the training features. Numeric columns will be standardized, and
                    categorical columns with dtype 'category' will be one-hot encoded.
    :param y_train: A pandas Series containing the training labels.
    :return: A tuple containing the trained logistic regression model (or any model inheriting from BaseEstimator) 
             and the preprocessor used for preprocessing the input features.
    """
    categorical_columns = X_train.select_dtypes(include=['category']).columns

    # Apply one-hot encoding to categorical columns and standard scaling to numeric columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), X_train.select_dtypes(exclude=['category']).columns),
            ('cat', OneHotEncoder(), categorical_columns)
        ])

    X_train_processed = preprocessor.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_processed, y_train)
    return model, preprocessor'''
        state_out, reward, done, info = env.step(user_code_string)
        expected_accuracy = 0.795 # Set this to an expected value for your specific dataset and model
        self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string = r'''
# Display the first five rows of X_train
print(X_train.head())

# Check for missing values in X_train
missing_values = X_train.isnull().sum()
missing_values
'''
        result = env.execute_user_code_lines(user_code_string)
        print(result)
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines_edge_case_one(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string = "'EXECUTE_LINES\n```\nimport numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn import preprocessing\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn import svm\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GridSearchCV\n```\n'"
        from agents import get_code_from_message
        user_code_string = get_code_from_message(user_code_string)
        result = env.execute_user_code_lines(user_code_string)
        # print(result)
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines_edge_case_two_isnull(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        subtask_running_code = '# Import necessary libraries\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler, OneHotEncoder\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.impute import SimpleImputer\n\n# Check for missing values\nmissing_values = X_train.isnull().sum()\nprint("Missing values: ", missing_values)\n\n# Identify categorical and numerical columns\ncategorical_cols = X_train.select_dtypes(include=[\'object\', \'category\']).columns\nnumerical_cols = X_train.select_dtypes(include=[\'int64\', \'float64\']).columns\n\n# Define preprocessing pipelines\nnumeric_transformer = Pipeline(steps=[\n    (\'imputer\', SimpleImputer(strategy=\'median\')),\n    (\'scaler\', StandardScaler())])\n\ncategorical_transformer = Pipeline(steps=[\n    (\'imputer\', SimpleImputer(strategy=\'most_frequent\')),\n    (\'onehot\', OneHotEncoder(handle_unknown=\'ignore\'))])\n\npreprocessor = ColumnTransformer(\n    transformers=[\n        (\'num\', numeric_transformer, numerical_cols),\n        (\'cat\', categorical_transformer, categorical_cols)])\n\n# Apply transformations to the data\nX_train_preprocessed = preprocessor.fit_transform(X_train)\n\n# Split the data into training and validation sets\nX_train, X_val, y_train, y_val = train_test_split(X_train_preprocessed, y_train, test_size=0.2, random_state=42)\n\n# Print the shapes of the training and validation sets\nprint("X_train shape: ", X_train.shape)\nprint("y_train shape: ", y_train.shape)\nprint("X_val shape: ", X_val.shape)\nprint("y_val shape: ", y_val.shape)'
        user_code_string_1 = 'EXECUTE_LINES(```\n# Import necessary libraries\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler, OneHotEncoder\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.impute import SimpleImputer\n\n# Check for missing values\nmissing_values = X_train.isnull().sum()\nprint("Missing values: ", missing_values)\n\n# Identify categorical and numerical columns\ncategorical_cols = X_train.select_dtypes(include=[\'object\', \'category\']).columns\nnumerical_cols = X_train.select_dtypes(include=[\'int64\', \'float64\']).columns\n\n# Define preprocessing pipelines\nnumeric_transformer = Pipeline(steps=[\n    (\'imputer\', SimpleImputer(strategy=\'median\')),\n    (\'scaler\', StandardScaler())])\n\ncategorical_transformer = Pipeline(steps=[\n    (\'imputer\', SimpleImputer(strategy=\'most_frequent\')),\n    (\'onehot\', OneHotEncoder(handle_unknown=\'ignore\'))])\n\npreprocessor = ColumnTransformer(\n    transformers=[\n        (\'num\', numeric_transformer, numerical_cols),\n        (\'cat\', categorical_transformer, categorical_cols)])\n\n# Apply transformations to the data\nX_train_preprocessed = preprocessor.fit_transform(X_train)\n\nprint("Preprocessing done.")\n```)'
        from agents import get_code_from_message
        user_code_string_1 = get_code_from_message(user_code_string_1)
        if subtask_running_code:
            # code = subtask_running_code + f'\n{user_code_string_1}'
            code = user_code_string_1
        result = env.execute_user_code_lines(code)
        print(result)
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines_edge_case_three(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string_1 = 'It seems like there is still an issue with the encoding of the categorical features. The error message suggests that the \'<0\' string cannot be converted to a float, which indicates that one or more categorical features have not been properly encoded. \n\nLet\'s modify the code to print out the unique values of the categorical features before and after encoding to ensure that they have been correctly transformed into numerical values.\n\nEXECUTE_LINES(```\nimport pandas as pd\nimport numpy as np\nfrom sklearn.preprocessing import LabelEncoder\nfrom imblearn.over_sampling import SMOTE\nfrom sklearn.preprocessing import StandardScaler\n\n# Check the shape of the dataset\nprint("Shape of the dataset: ", X_train.shape)\n\n# Check for missing values\nmissing_values = X_train.isnull().sum()\nprint("Missing values: ", missing_values[missing_values > 0])\n\n# Check the data types of the features\nprint("Data types: ", X_train.dtypes)\n\n# Encode categorical features\ncategorical_features = X_train.select_dtypes(include=[\'object\']).columns\nfor feature in categorical_features:\n    print(f"Unique values in {feature} before encoding: ", X_train[feature].unique())\n    le = LabelEncoder()\n    X_train[feature] = le.fit_transform(X_train[feature])\n    print(f"Unique values in {feature} after encoding: ", X_train[feature].unique())\n\n# Check the distribution of the target variable\nprint("Target variable distribution: ", y_train.value_counts(normalize=True))\n\n# Handle class imbalance\nsmote = SMOTE(random_state=42)\nX_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)\n\n# Check the distribution of the target variable after handling class imbalance\nprint("Target variable distribution after SMOTE: ", pd.Series(y_train_resampled).value_counts(normalize=True))\n\n# Check the correlation between the features\ncorrelation = X_train.corr()\nprint("Correlation between features: ", correlation)\n\n# Standardize numerical features\nnumerical_features = X_train.select_dtypes(include=[\'int64\', \'float64\']).columns\nscaler = StandardScaler()\nX_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])\n\n# Print the shape of the dataset after preprocessing\nprint("Shape of the dataset after preprocessing: ", X_train.shape)\n```)'
        from agents import get_code_from_message
        code = get_code_from_message(user_code_string_1)
        try:
            result = env.execute_user_code_lines(code)
        except Exception as e:
            result = f'{e.args[0]}'
        print(f'Code Output: {result}')
        print('')
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines_edge_case_four(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        code = """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE

# Check the shape of the dataset
print("Shape of the dataset: ", X_train.shape)

# Check for missing values
missing_values = X_train.isnull().sum()
print("Missing values: ", missing_values)

# Check the balance of the target variable
class_balance = y_train.value_counts()
print("Class balance: ", class_balance)

# If classes are imbalanced, use SMOTE for oversampling the minority class
if class_balance[0] / class_balance[1] > 1.5:
    smote = SMOTE()
    X_train, y_train = smote.fit_resample(X_train, y_train)

# Perform label encoding on categorical variables
categorical_features = X_train.select_dtypes(include=['object']).columns
le = LabelEncoder()
for feature in categorical_features:
    X_train[feature] = le.fit_transform(X_train[feature])

# Standardize numerical features
numerical_features = X_train.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Print the shapes of the new datasets
print("Shape of the training set: ", X_train.shape)
print("Shape of the validation set: ", X_val.shape)
"""
        user_code_string_1 = """
It seems there was an error in the code execution. The error message is not clear, but it could be due to the imbalance in the classes. Let's try to handle the imbalance using SMOTE and then proceed with the model training. 

EXECUTE_LINES(```
from imblearn.over_sampling import SMOTE

# Handle class imbalance
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Initialize XGBoost classifier
model = XGBClassifier()

# Fit the model on the resampled training data
model.fit(X_train_res, y_train_res)

# Predict on the resampled training set
y_train_pred = model.predict(X_train_res)

# Calculate and print the accuracy on the resampled training set
train_accuracy = accuracy_score(y_train_res, y_train_pred)
print("Training accuracy: ", train_accuracy)
```)
"""
        from agents import get_code_from_message
        code_1 = get_code_from_message(user_code_string_1)
        code = f'{code}\n{code_1}'
        try:
            result = env.execute_user_code_lines(code)
        except Exception as e:
            result = f'{e.args[0]}'
        print(f'Code Output: {result}')
        print('')
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_wdbc_edge_case_one(self):
        config = {'dataset_id': 'wdbc'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        code = """
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Check the distribution of the target variable
class_distribution = y_train.value_counts(normalize=True)
print("Class Distribution:\n", class_distribution)

# Check for missing values
missing_values = X_train.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Perform feature scaling
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)

# Check the range of values for each feature after scaling
scaled_features_range = X_train_scaled.describe().loc[['min', 'max']]
print("\nScaled Features Range:\n", scaled_features_range)
"""
        try:
            result = env.execute_user_code_lines(code)
        except Exception as e:
            result = f'{e.args[0]}'
        print(f'Code Output: {result}')
        print('')
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_credit_g_execute_lines_edge_case_three_first_relentless_output(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string_1 = "from typing import Tuple\nfrom pandas import DataFrame, Series\nfrom sklearn.base import BaseEstimator\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.impute import SimpleImputer\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\nimport pandas as pd\nimport numpy as np\n\ndef train_model(X_train: DataFrame, y_train: Series) -> Tuple[BaseEstimator, ColumnTransformer]:\n    # Identify categorical and numerical columns\n    categorical_cols = X_train.select_dtypes(include=['object', 'bool']).columns\n    numerical_cols = X_train.select_dtypes(include=['int64', 'float64']).columns\n\n    # Define preprocessing pipelines\n    numeric_transformer = Pipeline(steps=[\n        ('imputer', SimpleImputer(strategy='median')),\n        ('scaler', StandardScaler())])\n\n    categorical_transformer = Pipeline(steps=[\n        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),\n        ('onehot', OneHotEncoder(handle_unknown='ignore'))])\n\n    preprocessor = ColumnTransformer(\n        transformers=[\n            ('num', numeric_transformer, numerical_cols),\n            ('cat', categorical_transformer, categorical_cols)])\n\n    # Apply transformations to the data\n    X_train_preprocessed = preprocessor.fit_transform(X_train)\n\n    # Convert the target labels to {0, 1}\n    le = LabelEncoder()\n    y_train_encoded = le.fit_transform(y_train)\n\n    # Define the model\n    model = RandomForestClassifier(random_state=42)\n\n    # Train the model\n    model.fit(X_train_preprocessed, y_train_encoded)\n\n    return model, preprocessor"
        code = user_code_string_1
        state_out, reward, done, info = env.step(code)
        expected_accuracy = 0.64 # Set this to an expected value for your specific dataset and model
        self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed
        # self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed


    def test_environment_credit_g_execute_lines_edge_case_invalid_syntax(self):
        config = {'dataset_id': 'credit-g'}
        env = DataScienceEnvironment(config, None, 'data-science-credit-g')
        env.seed(42)
        env.reset()

        user_code_string = "'EXECUTE_LINES\n```\nimport numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import train_test_split\nfrom sklearn import preprocessing\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn import svm\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.linear_model impafort LogisticRegression\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix\nfrom sklearn.model_selection import cross_val_score\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GridSearchCV\n```\n'"
        from agents import get_code_from_message
        user_code_string = get_code_from_message(user_code_string)
        with self.assertRaises(Exception) as context:
            env.execute_user_code_lines(user_code_string)

        self.assertIn('SyntaxError', context.exception.args[0])  

    def test_environment_monks_problems_2(self):
        config = {'dataset_id': 'monks-problems-2'}
        env = DataScienceEnvironment(config, None, 'data-science-monks-problems-2')
        env.seed(42)
        env.reset()

        user_code_string = r'''
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

def train_model(X_train, y_train):
    # Identify categorical columns
    categorical_columns = X_train.select_dtypes(include=['category']).columns

    # Apply one-hot encoding to categorical columns and standard scaling to numeric columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), X_train.select_dtypes(exclude=['category']).columns),
            ('cat', OneHotEncoder(), categorical_columns)
        ])

    X_train_processed = preprocessor.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_processed, y_train)
    return model, preprocessor'''
        state_out, reward, done, info = env.step(user_code_string)
        expected_accuracy = 0.5702479338842975 # Set this to an expected value for your specific dataset and model
        self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_environment_monks_problems_2_relentless(self):
        config = {'dataset_id': 'monks-problems-2'}
        env = DataScienceEnvironment(config, None, 'data-science-monks-problems-2')
        env.seed(42)
        env.reset()

        user_code_string = r'''
from typing import Tuple
from pandas import DataFrame, Series
from sklearn.base import BaseEstimator
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def train_model(X_train: DataFrame, y_train: Series) -> Tuple[BaseEstimator, ColumnTransformer]:
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)

    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train_imputed), columns=X_train.columns)

    # Handle imbalanced dataset
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)

    # Split the dataset into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X_train_res, y_train_res, test_size=0.2, random_state=42)

    # Convert the labels to integer format
    y_train = y_train.astype(int)
    y_val = y_val.astype(int)

    # Initialize the models
    models = {
        "Logistic Regression": LogisticRegression(random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "XGBoost": XGBClassifier(random_state=42),
        "LightGBM": LGBMClassifier(random_state=42)
    }

    # Train the models and evaluate their performance
    best_model = None
    best_score = 0
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        score = roc_auc_score(y_val, y_pred)
        if score > best_score:
            best_score = score
            best_model = model

    # Preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', imputer, X_train.columns),
            ('scale', scaler, X_train.columns)
        ]
    )

    return best_model, preprocessor'''
        state_out, reward, done, info = env.step(user_code_string)
        expected_accuracy = 0.5702479338842975 # Set this to an expected value for your specific dataset and model
        self.assertAlmostEqual(reward, expected_accuracy, delta=0.01) # Adjust delta as needed

    def test_get_env(self):
        from utils.exp_utils import to_dot_dict
        config = {'setup': {'data_science_env_use_description': False}}
        env = get_env('data-science-iris', to_dot_dict(config), None)
        self.assertIsInstance(env, DataScienceEnvironment)


if __name__ == "__main__":
    # unittest.main()
    # TestEnvironment().test_environment_credit_g()
    # TestEnvironment().test_environment_credit_g_execute_lines()
    # TestEnvironment().test_environment_credit_g_execute_lines_edge_case_invalid_syntax()
    # TestEnvironment().test_environment_credit_g_execute_lines_edge_case_two_isnull()
    # TestEnvironment().test_environment_credit_g_execute_lines_edge_case_three()
    # TestEnvironment().test_environment_credit_g_execute_lines_edge_case_four()
    # TestEnvironment().test_environment_credit_g_execute_lines_edge_case_three_first_relentless_output()
    # TestEnvironment().test_environment_credit_g()
    # TestEnvironment().test_environment_monks_problems_2_relentless()
    TestEnvironment().test_environment_wdbc_edge_case_one()
    # TestEnvironment().test_get_env()


    # # Testing
    # y_true = ['good', 'bad', 'good', 'bad']
    # y_pred_1 = [1, 0, 1, 0]
    # y_pred_2 = ['good', 'bad', 'good', 'good']

    # print(robust_accuracy(y_true, y_pred_1)) # This should give the correct accuracy
    # print(robust_accuracy(y_true, y_pred_2)) # This should give the correct accuracy
