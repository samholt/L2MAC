"""
This is an example of how to generate a simple blackjack game using l2mac.
"""
from l2mac import generate_codebase

codebase: dict = generate_codebase(
    "Create a simple playable blackjack cli game", steps=2, run_tests=True)

# it will print the codebase (repo) complete with all the files as a dictionary
print(
    codebase
)
