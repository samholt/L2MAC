import pytest
import random
import string

from recipe_platform import RecipeSubmission

def test_recipe_submission():
	# Generate random data for recipe submission
	title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	ingredients = ['ingredient1', 'ingredient2']
	instructions = "Mix and cook"
	image = "image_url"

	submission = RecipeSubmission(title, ingredients, instructions, image)
	assert submission.is_valid()

def test_recipe_categorization():
	categories = ['Italian', 'Gluten-Free']
	submission = RecipeSubmission(title="Pizza", ingredients=['ingredient1', 'ingredient2'], instructions="Mix and cook", image="image_url", categories=categories)
	assert submission.has_valid_categories()

def test_recipe_edit_delete():
	recipe_id = random.randint(1, 1000)
	submission = RecipeSubmission.get_by_id(recipe_id)
	if submission is not None:
		submission.edit(title="New Title")
		assert submission.title == "New Title"

		submission.delete()
		assert RecipeSubmission.get_by_id(recipe_id) is None

def test_recipe_format_validation():
	incomplete_data = {
		'title': '',
		'ingredients': [],
		'instructions': "",
		'image': ""
	}
	submission = RecipeSubmission(**incomplete_data)
	assert not submission.is_valid()

def test_recipe_search():
	search_query = "chocolate"
	search_result = RecipeSubmission.search(search_query)
	assert all(search_query in recipe.title for recipe in search_result)

def test_recipe_categorization_search():
	category = 'Vegan'
	search_result = RecipeSubmission.search_by_category(category)
	assert all(category in recipe.categories for recipe in search_result)
