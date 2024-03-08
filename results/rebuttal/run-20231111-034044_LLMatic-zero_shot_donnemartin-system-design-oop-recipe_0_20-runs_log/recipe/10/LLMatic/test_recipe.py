import pytest
from recipe import Recipe


def test_search_recipes():
	recipe1 = Recipe('Pasta', ['pasta', 'tomato sauce'], 'Cook pasta. Add sauce.', [], ['Italian', 'Main Course'])
	recipe2 = Recipe('Salad', ['lettuce', 'tomato'], 'Mix ingredients.', [], ['Appetizer'])
	recipes = [recipe1, recipe2]
	assert Recipe.search_recipes(recipes, 'Pasta') == [recipe1]
	assert set(Recipe.search_recipes(recipes, 'tomato')) == set([recipe2])
	assert Recipe.search_recipes(recipes, 'Appetizer') == [recipe2]


def test_categorize_recipes():
	recipe1 = Recipe('Pasta', ['pasta', 'tomato sauce'], 'Cook pasta. Add sauce.', [], ['Italian', 'Main Course'])
	recipe2 = Recipe('Salad', ['lettuce', 'tomato'], 'Mix ingredients.', [], ['Appetizer'])
	recipes = [recipe1, recipe2]
	assert Recipe.categorize_recipes(recipes, 'Italian') == [recipe1]
	assert Recipe.categorize_recipes(recipes, 'Main Course') == [recipe1]
	assert Recipe.categorize_recipes(recipes, 'Appetizer') == [recipe2]

