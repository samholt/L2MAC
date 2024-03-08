import pytest
from recipe import Recipe


def test_recipe_methods():
	recipe = Recipe('testrecipe', 'testingredients', 'testinstructions', 'testimages', 'testcategory')
	assert recipe.submit_recipe() == 'Recipe submitted successfully'
	assert recipe.edit_recipe({'name': 'newrecipe', 'ingredients': 'newingredients', 'instructions': 'newinstructions', 'images': 'newimages', 'category': 'newcategory'}) == 'Recipe edited successfully'
	assert recipe.delete_recipe() == 'Recipe deleted successfully'
	assert recipe.name == 'testrecipe'
	assert recipe.ingredients == 'testingredients'
	assert recipe.instructions == 'testinstructions'
	assert recipe.images == 'testimages'
	assert recipe.category == 'testcategory'
	assert recipe.recipe_db == {}
	assert recipe.validate_recipe() is True
	assert recipe.search_recipe('test') == {}
	assert recipe.categorize_recipe('test') == {}
	recipe.add_rating(5)
	assert recipe.calculate_average_rating() == 5
