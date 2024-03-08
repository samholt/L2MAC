from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer, TextStreamer
import torch
from time import time

t0 = time()
model_path="tiiuae/falcon-7b-instruct"
# model_path="ehartford/WizardLM-33B-V1.0-Uncensored"
# model_path="tiiuae/falcon-40b-instruct"
# model_path="ehartford/Wizard-Vicuna-30B-Uncensored"
# model_path="TheBloke/Wizard-Vicuna-13B-Uncensored-HF"
# model_path="TheBloke/Wizard-Vicuna-7B-Uncensored-HF"
# model_path="xzuyn/LLaMa-Open-Instruct-Uncensored-70K-7B-Merged"
# model_path="ehartford/Wizard-Vicuna-7B-Uncensored"



# from transformers import AutoTokenizer, LlamaForCausalLM

# model = LlamaForCausalLM.from_pretrained(model_path)
# tokenizer = AutoTokenizer.from_pretrained(model_path)

# prompt = "Hey, are you conscious? Can you talk to me?"
# inputs = tokenizer(prompt, return_tensors="pt")

# # Generate
# generate_ids = model.generate(inputs.input_ids, max_length=30)
# print(tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])

PARAMS = dict(top_k=10,
            num_return_sequences=1,
            do_sample=True,
            max_length=10000,
            # temperature=1.0,
            )


print('A: ', time() - t0)
config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, load_in_4bit=True, device_map="auto")
model = AutoModelForCausalLM.from_pretrained(model_path,
                                             trust_remote_code=True,
                                            #  load_in_4bit=True,
                                             device_map="auto",
                                             torch_dtype=torch.float16,
                                             )
tokenizer = AutoTokenizer.from_pretrained(model_path)
print('B: ', time() - t0)

streamer = TextStreamer(tokenizer)
print('C: ', time() - t0)
# input_text = "Write me an autoGPT prompt for running a small newsletter business."
input_text = input('Enter a prompt: ')
input_text =  f"""
USER: {input_text}
ASSISTANT:"""

input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
print('D: ', time() - t0)
outputs = model.generate(input_ids, streamer=streamer, **PARAMS)
output = tokenizer.decode(outputs[0])
# print(output)
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

while True:
    output_mod = output.replace('<s>', '').replace('</s>', '')
    input_text = input('Enter a prompt: ')
    input_text =  f"""
{output_mod}
USER: {input_text}
ASSISTANT:"""
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
    outputs = model.generate(input_ids, streamer=streamer, **PARAMS)
    output = tokenizer.decode(outputs[0])
    # print(output)