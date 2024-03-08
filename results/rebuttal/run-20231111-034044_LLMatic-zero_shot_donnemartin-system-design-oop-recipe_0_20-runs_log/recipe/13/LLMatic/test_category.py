import pytest
from category import Category
from recipe import Recipe

@pytest.fixture

def mock_database():
	return [
		Recipe('Pancakes', ['flour', 'milk', 'eggs'], 'Mix ingredients and cook on pan', [], ['breakfast', 'American', 'vegetarian']),
		Recipe('Spaghetti Bolognese', ['spaghetti', 'minced meat', 'tomato sauce'], 'Cook spaghetti and sauce separately, then mix', [], ['lunch', 'Italian', 'gluten']),
		Recipe('Salad', ['lettuce', 'tomatoes', 'cucumber'], 'Mix all ingredients', [], ['dinner', 'vegan', 'gluten-free'])
	]

def test_categorize_by_type(mock_database):
	category = Category(mock_database)
	assert len(category.categorize_by_type('breakfast')) == 1
	assert len(category.categorize_by_type('Nonexistent Type')) == 0

def test_categorize_by_cuisine(mock_database):
	category = Category(mock_database)
	assert len(category.categorize_by_cuisine('Italian')) == 1
	assert len(category.categorize_by_cuisine('Nonexistent Cuisine')) == 0

def test_categorize_by_dietary_needs(mock_database):
	category = Category(mock_database)
	assert len(category.categorize_by_dietary_needs('vegan')) == 1
	assert len(category.categorize_by_dietary_needs('Nonexistent Dietary Needs')) == 0
