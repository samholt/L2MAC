import pytest
from recipe import Recipe

def test_submit_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.submit_recipe() == True

def test_edit_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.edit_recipe() == True

def test_delete_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.delete_recipe() == True

def test_validate_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.validate_recipe() == True

def test_search_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.search_recipe('ingredient1') == False

def test_categorize_recipe():
	recipe = Recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], 'category')
	assert recipe.categorize_recipe('type', 'cuisine', 'dietary_needs') == False
