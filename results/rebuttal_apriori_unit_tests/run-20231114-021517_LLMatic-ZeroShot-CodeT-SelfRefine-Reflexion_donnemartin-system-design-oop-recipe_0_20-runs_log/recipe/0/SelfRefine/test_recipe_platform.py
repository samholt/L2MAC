import pytest
import random
import string

from recipe_platform import User, Admin, Recipe, Rating, Review

# Mock data
USERS = [User(i, f'user{i}', f'pass{i}') for i in range(1, 11)]
ADMINS = [Admin(i, f'admin{i}', f'pass{i}') for i in range(1, 3)]
RECIPES = [Recipe(i, f'recipe{i}', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url') for i in range(1, 101)]

# Tests

def test_recipe_submission():
	# Generate random data for recipe submission
	title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	ingredients = ['ingredient1', 'ingredient2']
	instructions = 'Mix and cook'
	image = 'image_url'

	submission = Recipe(101, title, ingredients, instructions, image)
	assert submission.is_valid()

# ... rest of the tests
