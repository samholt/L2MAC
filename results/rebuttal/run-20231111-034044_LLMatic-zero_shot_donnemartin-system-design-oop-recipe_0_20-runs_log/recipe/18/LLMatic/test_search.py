import pytest
from search import Search
from recipe import Recipe

def test_search_by_name():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]
	search = Search(recipe_db)
	assert search.search_by_name('Pasta') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]


def test_search_by_ingredient():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]
	search = Search(recipe_db)
	assert search.search_by_ingredient('Pasta') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]


def test_search_by_category():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]
	search = Search(recipe_db)
	assert search.search_by_category('Italian') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]


def test_categorize_by_type():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]
	search = Search(recipe_db)
	assert search.categorize_by_type('Main Course') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]


def test_categorize_by_cuisine():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]
	search = Search(recipe_db)
	assert search.categorize_by_cuisine('Italian') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course']}]


def test_categorize_by_diet():
	recipe_db = [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course', 'Vegetarian']}]
	search = Search(recipe_db)
	assert search.categorize_by_diet('Vegetarian') == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'categories': ['Italian', 'Main Course', 'Vegetarian']}]

