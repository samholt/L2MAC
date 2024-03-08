import pytest
from categories import Categories

def test_categories():
	categories = Categories()
	categories.add_category('type', 'Vegetarian')
	categories.add_category('cuisine', 'Italian')
	categories.add_category('dietary', 'Gluten-free')

	assert categories.get_categories('type') == ['Vegetarian']
	assert categories.get_categories('cuisine') == ['Italian']
	assert categories.get_categories('dietary') == ['Gluten-free']

	assert categories.categorize_recipe(1, 'type', 'Vegetarian') == {'recipe_id': 1, 'category_type': 'type', 'category': 'Vegetarian'}
	assert categories.categorize_recipe(1, 'cuisine', 'Italian') == {'recipe_id': 1, 'category_type': 'cuisine', 'category': 'Italian'}
	assert categories.categorize_recipe(1, 'dietary', 'Gluten-free') == {'recipe_id': 1, 'category_type': 'dietary', 'category': 'Gluten-free'}

	assert categories.categorize_recipe(1, 'type', 'Non-existent') == 'Category does not exist'

