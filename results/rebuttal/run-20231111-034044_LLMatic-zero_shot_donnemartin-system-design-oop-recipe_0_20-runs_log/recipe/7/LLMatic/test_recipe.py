import pytest
from recipe import Recipe

def test_submit_recipe():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan.', ['image1.jpg'], ['Breakfast'])
	assert recipe.submit_recipe() == True


def test_edit_recipe():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan.', ['image1.jpg'], ['Breakfast'])
	assert recipe.edit_recipe('Pancakes', ['Flour', 'Eggs', 'Milk', 'Sugar'], 'Mix ingredients and cook on pan. Add sugar on top.', ['image1.jpg'], ['Breakfast', 'Dessert']) == True


def test_delete_recipe():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan.', ['image1.jpg'], ['Breakfast'])
	recipe.submit_recipe()
	assert recipe.delete_recipe() == True


def test_validate_recipe():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan.', ['image1.jpg'], ['Breakfast'])
	assert recipe.validate_recipe() == True
	recipe = Recipe('', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan.', ['image1.jpg'], ['Breakfast'])
	assert recipe.validate_recipe() == False
