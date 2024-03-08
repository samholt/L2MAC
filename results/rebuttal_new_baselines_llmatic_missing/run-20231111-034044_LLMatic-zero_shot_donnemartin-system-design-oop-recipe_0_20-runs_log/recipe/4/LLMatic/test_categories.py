import pytest
from categories import Category

def test_add_category():
	category = Category()
	category.add_category('type', 'Vegetarian')
	assert 'Vegetarian' in category.get_categories('type')

def test_categorize_recipe():
	category = Category()
	category.add_category('type', 'Vegetarian')
	assert category.categorize_recipe(1, 'type', 'Vegetarian') == 'Recipe categorized successfully'
	assert category.categorize_recipe(1, 'type', 'Non-existent') == 'Invalid category'
