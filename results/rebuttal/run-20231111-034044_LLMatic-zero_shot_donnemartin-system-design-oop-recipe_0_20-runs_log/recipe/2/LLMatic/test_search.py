import pytest
from search import Search
from recipe import Recipe

def test_search_by_ingredient():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.search_by_ingredient('Cheese') == [recipes[0], recipes[1]]


def test_search_by_name():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.search_by_name('Pizza') == [recipes[0]]


def test_search_by_category():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.search_by_category('Main') == [recipes[0], recipes[1]]


def test_categorize_by_type():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.categorize_by_type('Main') == [recipes[0], recipes[1]]


def test_categorize_by_cuisine():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.categorize_by_cuisine('Italian') == [recipes[0], recipes[1]]


def test_categorize_by_diet():
	recipes = [Recipe('Pizza', ['Cheese', 'Tomato'], 'Bake', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian'), Recipe('Pasta', ['Cheese', 'Tomato'], 'Boil', 'Italian', 'Vegetarian', 'Main', 'Italian', 'Vegetarian')]
	search = Search(recipes)
	assert search.categorize_by_diet('Vegetarian') == [recipes[0], recipes[1]]

