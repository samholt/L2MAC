from transformers import AutoTokenizer
import transformers
import torch
from time import time

# model = "meta-llama/Llama-2-7b-chat-hf"
# tokenizer_model = "meta-llama/Llama-2-70b-chat-hf"
model = "meta-llama/Llama-2-70b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)
t0 = time()
sequences = pipeline(
    'I liked "Breaking Bad" and "Band of Brothers". Do you have any recommendations of other shows I might like?\n',
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
print('Time: ', time() - t0)