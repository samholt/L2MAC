from recipes import RecipeManager
from database import MockDatabase

def test_recipe_management():
	db = MockDatabase()
	recipe_manager = RecipeManager(db)

	# Test recipe submission
	recipe = recipe_manager.submit_recipe(1, 1, 'Chicken Soup', 'A delicious chicken soup recipe', 'chicken, soup', 'soup')
	assert recipe['recipe_id'] == 1
	assert recipe['user_id'] == 1
	assert recipe['title'] == 'Chicken Soup'
	assert recipe['description'] == 'A delicious chicken soup recipe'
	assert recipe['ingredients'] == 'chicken, soup'
	assert recipe['category'] == 'soup'
	assert recipe_manager.submit_recipe(1, 1, 'Chicken Soup', 'A delicious chicken soup recipe', 'chicken, soup', 'soup') == 'Recipe already exists'

	# Test recipe retrieval
	recipe = recipe_manager.get_recipe(1)
	assert recipe['user_id'] == 1
	assert recipe['title'] == 'Chicken Soup'
	assert recipe['description'] == 'A delicious chicken soup recipe'
	assert recipe['ingredients'] == 'chicken, soup'
	assert recipe['category'] == 'soup'

	# Test recipe editing
	assert recipe_manager.edit_recipe(1, title='Vegetable Soup', ingredients='vegetables, soup', category='vegetarian') == 'Recipe edited successfully'
	recipe = recipe_manager.get_recipe(1)
	assert recipe['title'] == 'Vegetable Soup'
	assert recipe['ingredients'] == 'vegetables, soup'
	assert recipe['category'] == 'vegetarian'

	# Test recipe deletion
	assert recipe_manager.delete_recipe(1) == 'Recipe deleted successfully'
	assert recipe_manager.get_recipe(1) == 'Recipe not found'

	# Test recipe search
	recipe_manager.submit_recipe(2, 1, 'Chicken Curry', 'A delicious chicken curry recipe', 'chicken, curry', 'curry')
	results = recipe_manager.search_recipes('curry')
	assert len(results) == 1
	assert results[2]['title'] == 'Chicken Curry'
