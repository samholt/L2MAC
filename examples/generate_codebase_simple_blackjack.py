from l2mac import generate_codebase

# run pip install pygame==2.1.2 (for best results)
codebase: dict = generate_codebase("Create a simple playable blackjack cli game", steps=2, run_tests=True)

print(codebase)  # it will print the codebase (repo) complete with all the files as a dictionary
