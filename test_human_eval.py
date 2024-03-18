from human_eval.data import write_jsonl, read_problems

from rate_limiter import ChatRateLimiter
from llm_utils import chat_completion_rl
rate_limiter = ChatRateLimiter(request_limit=200, token_limit=40000)

problems = read_problems()

num_samples_per_task = 1
for task_id in problems:
    completions = []
    for _ in range(num_samples_per_task):
        problem = problems[task_id]["prompt"]
        response = chat_completion_rl(
            # model="gpt-3.5-turbo",
            model="gpt-4",
            messages=[
                    {"role": "system", "content": "You are an expert coding agent solving the HumanEval coding benchmark. You are given a prompt and a test case. You must write code that passes the test case."},
                    {"role": "user", "content": f"Complete the following prompt: {problem}"}
                ],
            max_tokens=5000,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            # stop=["\n", "Human:", "AI:"],
            _use_azure_api=True,
            _rate_limiter=rate_limiter
            )
        print(response)
        print('---')
        completions.append(chat_completion_rl(problems[task_id]["prompt"], rate_limiter))
    problems[task_id]["completions"] = completions

samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)