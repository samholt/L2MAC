import torch
import transformers
from transformers import (
AutoTokenizer,
BitsAndBytesConfig,
AutoModelForCausalLM,
)
from time import time

model_name = "meta-llama/Llama-2-70b-chat-hf"
# model_name = "meta-llama/Llama-2-7b-chat-hf"
print(f"Loading {model_name}")

model = AutoModelForCausalLM.from_pretrained(model_name,        
                                            #  torch_dtype=torch.float16, 
                                            # load_in_8bit=True, 
                                            load_in_4bit=True, 
                                            device_map="auto", 
                                            trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)


pipeline = transformers.pipeline(
"text-generation",
model=model,
tokenizer=tokenizer,
trust_remote_code=True,
device_map="auto",
)
t0 = time()
sequences = pipeline(
    'I liked "Breaking Bad" and "Band of Brothers". Do you have any recommendations of other shows I might like?\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=1000,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
print('Time: ', time() - t0)