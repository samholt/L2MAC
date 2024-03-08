import pytest
from categories import Categories

def test_search_by_ingredient():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.search_by_ingredient('Cheese') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}, {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}]

def test_search_by_name():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.search_by_name('Pizza') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_search_by_category():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.search_by_category('Italian') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_type():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.categorize_by_type('Vegetarian') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_cuisine():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.categorize_by_cuisine('Italian') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]

def test_categorize_by_diet():
	categories = Categories()
	categories.recipes = {
		'1': {'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'},
		'2': {'name': 'Burger', 'ingredients': ['Bread', 'Beef', 'Cheese'], 'categories': ['American', 'Main Course'], 'type': 'Non-Vegetarian', 'cuisine': 'American', 'diet': 'Non-Vegetarian'}
	}
	assert categories.categorize_by_diet('Vegetarian') == [{'name': 'Pizza', 'ingredients': ['Flour', 'Tomato', 'Cheese'], 'categories': ['Italian', 'Main Course'], 'type': 'Vegetarian', 'cuisine': 'Italian', 'diet': 'Vegetarian'}]
