import pytest
from services import UserService, RecipeService
from models import User, Recipe


def test_user_service():
	user_service = UserService()

	# Test create user
	user = user_service.create_user('test_user', 'password', 'test@test.com', [])
	assert user.username == 'test_user'
	assert user.password == 'password'
	assert user.email == 'test@test.com'
	assert user.favorite_recipes == []
	assert user.submitted_recipes == []

	# Test get user
	user = user_service.get_user('test_user')
	assert user.username == 'test_user'

	# Test update user
	user = user_service.update_user('test_user', 'new_password', 'new_email@test.com', ['Pizza'])
	assert user.password == 'new_password'
	assert user.email == 'new_email@test.com'
	assert user.favorite_recipes == ['Pizza']

	# Test save favorite recipe
	user = user_service.save_favorite_recipe('test_user', 'Tacos')
	assert 'Tacos' in user.favorite_recipes

	# Test get user submitted recipes
	assert user_service.get_user_submitted_recipes('test_user') == []


def test_recipe_service():
	user_service = UserService()
	recipe_service = RecipeService()

	# Create a user
	user = user_service.create_user('test_user', 'password', 'test@test.com', [])

	# Test create recipe
	recipe = recipe_service.create_recipe('Pizza', ['Dough', 'Tomato Sauce', 'Cheese'], 'Bake it', 'pizza.jpg', ['Italian'], 'test_user')
	assert recipe.name == 'Pizza'
	assert recipe.ingredients == ['Dough', 'Tomato Sauce', 'Cheese']
	assert recipe.instructions == 'Bake it'
	assert recipe.image == 'pizza.jpg'
	assert recipe.categories == ['Italian']
	assert recipe.submitted_by == 'test_user'

	# Test get recipe
	recipe = recipe_service.get_recipe('Pizza')
	assert recipe.name == 'Pizza'

	# Test update recipe
	recipe = recipe_service.update_recipe('Pizza', ['Dough', 'Tomato Sauce', 'Cheese', 'Pepperoni'], 'Bake it', 'pizza.jpg', ['Italian'], 'test_user')
	assert recipe.ingredients == ['Dough', 'Tomato Sauce', 'Cheese', 'Pepperoni']

	# Test delete recipe
	recipe_service.delete_recipe('Pizza')
	assert recipe_service.get_recipe('Pizza') is None

	# Test get all recipes
	assert recipe_service.get_all_recipes() == []

	# Test get recipe count
	assert recipe_service.get_recipe_count() == 0

	# Test get recipe recommendations
	assert recipe_service.get_recipe_recommendations(user) == []

