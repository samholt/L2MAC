import pytest

from search import Search
from recipe import Recipe


def test_search_by_name():
	recipes = [Recipe('Pasta', ['Tomato', 'Pasta'], 'Boil pasta, add sauce', ['image1.jpg'], 'Italian'), Recipe('Pizza', ['Tomato', 'Cheese', 'Dough'], 'Bake dough, add toppings', ['image2.jpg'], 'Italian')]
	search = Search(recipes)
	assert len(search.search_by_name('Pasta')) == 1
	assert len(search.search_by_name('Pizza')) == 1
	assert len(search.search_by_name('Burger')) == 0


def test_search_by_category():
	recipes = [Recipe('Pasta', ['Tomato', 'Pasta'], 'Boil pasta, add sauce', ['image1.jpg'], 'Italian'), Recipe('Pizza', ['Tomato', 'Cheese', 'Dough'], 'Bake dough, add toppings', ['image2.jpg'], 'Italian')]
	search = Search(recipes)
	assert len(search.search_by_category('Italian')) == 2
	assert len(search.search_by_category('Mexican')) == 0
