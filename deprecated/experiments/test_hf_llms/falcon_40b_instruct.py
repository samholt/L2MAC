from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
# from accelerate import Accelerator
from time import time

t0 = time()
model = "tiiuae/falcon-40b-instruct"

# accelerator = Accelerator(cpu=True)
tokenizer = AutoTokenizer.from_pretrained(model)
print('A: ', time() - t0)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    load_in_4bit=True,
    # device='cpu',
)
print('B: ', time() - t0)
sequences = pipeline(
   "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
print('C: ', time() - t0)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
print('D: ', time() - t0)