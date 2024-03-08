import pytest
from search import Search
from recipe import Recipe

@pytest.fixture

def mock_database():
	return [
		Recipe('Pancakes', ['flour', 'milk', 'eggs'], 'Mix ingredients and cook on pan', [], ['breakfast', 'American', 'vegetarian']),
		Recipe('Spaghetti Bolognese', ['spaghetti', 'minced meat', 'tomato sauce'], 'Cook spaghetti and sauce separately, then mix', [], ['lunch', 'Italian', 'gluten']),
		Recipe('Salad', ['lettuce', 'tomatoes', 'cucumber'], 'Mix all ingredients', [], ['dinner', 'vegan', 'gluten-free'])
	]

def test_search_by_name(mock_database):
	search = Search(mock_database)
	assert len(search.search_by_name('Pancakes')) == 1
	assert len(search.search_by_name('Nonexistent Recipe')) == 0

def test_search_by_ingredient(mock_database):
	search = Search(mock_database)
	assert len(search.search_by_ingredient('flour')) == 1
	assert len(search.search_by_ingredient('Nonexistent Ingredient')) == 0

def test_search_by_category(mock_database):
	search = Search(mock_database)
	assert len(search.search_by_category('breakfast')) == 1
	assert len(search.search_by_category('Nonexistent Category')) == 0
