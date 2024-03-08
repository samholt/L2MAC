from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer
import torch
from time import time

t0 = time()
model_path="tiiuae/falcon-40b-instruct"

print('A: ', time() - t0)
config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, load_in_4bit=True, device_map="auto")
print('B: ', time() - t0)

tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-40b-instruct")
print('C: ', time() - t0)
# input_text = "Write me an autoGPT prompt for running a small newsletter business."
input_text = input('Enter a prompt: ')
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
print('D: ', time() - t0)
outputs = model.generate(input_ids, max_length=100)
output = tokenizer.decode(outputs[0])
print(output)
output_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
outputs = model.generate(input_ids, decoder_input_ids=output_ids, max_length=100)
output = tokenizer.decode(outputs[0])
print(output)
# input_text = "How to do accounts."
# input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
# print('D: ', time() - t0)
# outputs = model.generate(input_ids, max_length=100)
# print(tokenizer.decode(outputs[0]))

print('E: ', time() - t0)