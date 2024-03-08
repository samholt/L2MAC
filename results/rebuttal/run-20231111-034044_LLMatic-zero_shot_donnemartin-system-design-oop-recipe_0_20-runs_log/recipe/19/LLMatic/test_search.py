import pytest
from search import Search
from recipe import Recipe


def test_search_by_name():
	search = Search()
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['image1.jpg'], ['Breakfast'])
	search.db['Pancakes'] = recipe
	assert search.search_by_name('Pancakes') == [recipe]


def test_search_by_ingredients():
	search = Search()
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['image1.jpg'], ['Breakfast'])
	search.db['Pancakes'] = recipe
	assert search.search_by_ingredients(['Flour', 'Eggs']) == [recipe]


def test_search_by_category():
	search = Search()
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['image1.jpg'], ['Breakfast'])
	search.db['Pancakes'] = recipe
	assert search.search_by_category('Breakfast') == [recipe]
