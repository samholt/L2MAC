from l2mac import generate_codebase

codebase: dict = generate_codebase(
    "Create a beautiful, playable and simple snake game with pygame. Make the snake and food be aligned to the same 10-pixel grid.",
    steps=2,
    run_tests=True,
)

print(codebase)  # it will print the codebase (repo) complete with all the files as a dictionary
