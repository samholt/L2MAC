import pytest
from search import Search

@pytest.fixture

def setup_database():
	return {
		'1': {'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'},
		'2': {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'},
		'3': {'name': 'Burger', 'ingredients': ['bun', 'meat', 'cheese'], 'category': 'American'}
	}

@pytest.fixture

def setup_search(setup_database):
	return Search(setup_database)


def test_search_by_ingredient(setup_search):
	results = setup_search.search_by_ingredient('tomato')
	assert len(results) == 2
	assert 'Pasta' in [recipe['name'] for recipe in results]
	assert 'Pizza' in [recipe['name'] for recipe in results]


def test_search_by_name(setup_search):
	results = setup_search.search_by_name('Pasta')
	assert len(results) == 1
	assert 'Pasta' in [recipe['name'] for recipe in results]


def test_search_by_category(setup_search):
	results = setup_search.search_by_category('Italian')
	assert len(results) == 2
	assert 'Pasta' in [recipe['name'] for recipe in results]
	assert 'Pizza' in [recipe['name'] for recipe in results]
