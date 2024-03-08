import pytest
from recipe import Recipe


def test_submit_recipe():
	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', 'category1')
	assert recipe.submit_recipe() == 'Recipe submitted successfully'


def test_edit_recipe():
	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', 'category1')
	recipe.submit_recipe()
	new_recipe = {'ingredients': ['ingredient2'], 'instructions': 'instructions2', 'images': 'image2', 'categories': 'category2'}
	assert recipe.edit_recipe(new_recipe) == 'Recipe edited successfully'


def test_delete_recipe():
	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', 'category1')
	recipe.submit_recipe()
	assert recipe.delete_recipe() == 'Recipe deleted successfully'


def test_validate_recipe_format():
	recipe = Recipe('', ['ingredient1'], 'instructions1', 'image1', 'category1')
	assert not recipe.validate_recipe_format()

	recipe = Recipe('recipe1', [], 'instructions1', 'image1', 'category1')
	assert not recipe.validate_recipe_format()

	recipe = Recipe('recipe1', ['ingredient1'], '', 'image1', 'category1')
	assert not recipe.validate_recipe_format()

	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', '', 'category1')
	assert not recipe.validate_recipe_format()

	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', '')
	assert not recipe.validate_recipe_format()

	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', 'category1')
	assert recipe.validate_recipe_format()


def test_share_recipe():
	recipe = Recipe('recipe1', ['ingredient1'], 'instructions1', 'image1', 'category1')
	assert recipe.share_recipe('Facebook') == 'Recipe recipe1 shared on Facebook'
