from human_eval.data import write_jsonl, read_problems

problems = read_problems()

print(problems['HumanEval/97']['task_id'])
print(problems['HumanEval/97']['prompt'])
print(problems['HumanEval/97']['entry_point'])
print(problems['HumanEval/97']['canonical_solution'])
print(problems['HumanEval/97']['test'])

num_samples_per_task = 200
samples = [
    dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("samples.jsonl", samples)