from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

agent_executor = create_python_agent(
    # llm=OpenAI(temperature=0, max_tokens=1000, model_name="gpt-3.5-turbo"),
    # llm=OpenAI(temperature=0, max_tokens=1000),
    # llm=ChatOpenAI(temperature=0, max_tokens=1000, model_name="gpt-3.5-turbo"),
    llm=ChatOpenAI(temperature=0, max_tokens=1000, model_name="gpt-4"),
    # tool=PythonREPLTool(python_repl=PythonREPL(_globals=globals(), _locals=None)),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# agent_executor.run(
#     """Understand, write a single neuron neural network in PyTorch.
# Take synthetic data for y=2x. Train for 1000 epochs and print every 100 epochs.
# Return prediction for x = 5"""
# )
# agent_executor.run(
# """
# You are an automated expert Data Scientist.
# Load the local file './data/iris/iris.csv', create and run a classifier to predict the iris variety, with a hold out test set of 20%. Print the accuracy of the model."""
# )
agent_executor.run(
"""
You are an automated expert Data Scientist.
In this challenge, we ask you to build a predictive model who survives using passenger data (ie name, age, gender, socio-economic class, etc).
In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. One dataset is titled ./data/titanic/train.csv and the other is titled ./data/titanic/test.csv.

Train.csv will contain the details of a subset of the passengers on board (891 to be exact) and importantly, will reveal whether they survived or not, also known as the “ground truth”.

The test.csv dataset contains similar information but does not disclose the “ground truth” for each passenger. It’s your job to predict these outcomes.

Using the patterns you find in the ./data/titanic/train.csv data, predict whether the other 418 passengers on board (found in test.csv) survived.
Submission File Format:
You should submit a csv file with exactly 418 entries plus a header row. Your submission will show an error if you have extra columns (beyond PassengerId and Survived) or rows.

The file should have exactly 2 columns:

PassengerId (sorted in any order)."""
)