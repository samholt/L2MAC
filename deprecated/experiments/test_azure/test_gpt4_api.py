#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://vdslabazuremloai-uksouth.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

prompt = """
You are an automated expert Data Scientist.
In this challenge, we ask you to build a predictive model who survives using passenger data (ie name, age, gender, socio-economic class, etc).
In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. One dataset is titled ./data/titanic/train.csv and the other is titled ./data/titanic/test.csv.

Train.csv will contain the details of a subset of the passengers on board (891 to be exact) and importantly, will reveal whether they survived or not, also known as the “ground truth”.

The test.csv dataset contains similar information but does not disclose the “ground truth” for each passenger. It’s your job to predict these outcomes.

Using the patterns you find in the ./data/titanic/train.csv data, predict whether the other 418 passengers on board (found in test.csv) survived.
Submission File Format:
You should submit a csv file with exactly 418 entries plus a header row. Your submission will show an error if you have extra columns (beyond PassengerId and Survived) or rows.

The file should have exactly 2 columns:

PassengerId (sorted in any order).
Understand the problem, by creating a step-by-step plan. Then execute each step on this plan, with a specific prompt for a separate GPT agent model. Create additional tests, checks and evaluation metrics on the validation dataset to help make excellent model.
"""\

response = openai.ChatCompletion.create(
  engine="gpt4_20230815",
  messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)


# response = openai.Completion.create(
#   engine="gpt35turbo_20230727",
#   prompt=prompt,
#   temperature=1,
#   max_tokens=1000,
#   top_p=0.5,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=None)

print(response)
print('')