from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer, TextStreamer
import torch
from time import time

t0 = time()
# model_path="meta-llama/Llama-2-70b-chat-hf"
model_path="meta-llama/Llama-2-7b-chat-hf"

print('A: ', time() - t0)
config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, load_in_4bit=True, device_map="auto")
model = AutoModelForCausalLM.from_pretrained(model_path,
                                            #  trust_remote_code=True,
                                            #  load_in_4bit=True,
                                             device_map="auto"
                                            #  device_map="cuda:0"
                                             )
print('B: ', time() - t0)

tokenizer = AutoTokenizer.from_pretrained(model_path)
streamer = TextStreamer(tokenizer)
print('C: ', time() - t0)
# input_text = "Write me an autoGPT prompt for running a small newsletter business."
input_text = input('Enter a prompt: ')
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
print('D: ', time() - t0)
outputs = model.generate(input_ids, streamer=streamer, max_length=10000,  
    do_sample=True,
    top_k=10,
    num_return_sequences=1) #, temperature=1.0)
output = tokenizer.decode(outputs[0])
print(output)
# output_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
# outputs = model.generate(input_ids, decoder_input_ids=output_ids, max_length=100)
# output = tokenizer.decode(outputs[0])
# print(output)
# input_text = "How to do accounts."
# input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
# print('D: ', time() - t0)
# outputs = model.generate(input_ids, max_length=100)
# print(tokenizer.decode(outputs[0]))
print('E: ', time() - t0)