import pytest
from categories import Categories

def test_search_by_ingredient():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.search_by_ingredient('Cheese') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_search_by_name():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.search_by_name('Pizza') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_search_by_category():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.search_by_category('Italian') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_type():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.categorize_by_type('Main') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_cuisine():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.categorize_by_cuisine('Italian') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_diet():
	categories = Categories()
	categories.add_recipe('1', {'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'})
	assert categories.categorize_by_diet('Vegetarian') == [{'name': 'Pizza', 'ingredients': ['Cheese', 'Tomato'], 'categories': ['Italian'], 'type': 'Main', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

