"""
This example demonstrates how to generate a book using the `generate_book`
function.
"""
from l2mac import generate_book

book: dict = generate_book(
    r"""
Write a complete recipe book for the following book title of "Twirls & Tastes:
A Journey Through Italian Pasta"

Description: "Twirls & Tastes" invites you on a flavorful expedition across
Italy, exploring the diverse pasta landscape from the sun-drenched hills of
Tuscany to the bustling streets of Naples. Discover regional specialties,
learn the stories behind each dish, and master the art of pasta making with
easy-to-follow recipes that promise to delight your senses.
""",
    steps=30,
)

print(
    book
)  # it will print the book folder complete with all the files as a dictionary
