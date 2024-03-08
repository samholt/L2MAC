import pytest
from models.recipe import Recipe
from services.recipe_service import RecipeService

def test_create_recipe():
	recipe = Recipe(id='1', name='test', ingredients=[], instructions=[], images=[], categories=[], user_id='1', ratings=[], reviews=[])
	RecipeService.create_recipe(recipe)
	assert RecipeService.get_recipe('1') == recipe

def test_update_recipe():
	recipe = Recipe(id='1', name='test_updated', ingredients=[], instructions=[], images=[], categories=[], user_id='1', ratings=[], reviews=[])
	RecipeService.update_recipe(recipe)
	assert RecipeService.get_recipe('1') == recipe

def test_delete_recipe():
	RecipeService.delete_recipe('1')
	assert RecipeService.get_recipe('1') is None
