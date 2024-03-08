import pytest
from recommendations import Recommendation
from users import UserManager
from recipes import Recipe


def test_recommendations():
	users = UserManager()
	recipes = Recipe()
	recommendations = Recommendation(users, recipes)

	# Create a user and a recipe
	users.create_user('1', 'Test User', 'test@example.com')
	recipes.submit_recipe('1', {'name': 'Test Recipe', 'category': 'Test Category', 'ingredients': ['Test Ingredient']})

	# The user likes the recipe
	users.get_user('1').liked_recipes.append(recipes.get_recipe('1'))

	# The recommendation system should recommend the recipe the user liked
	assert recommendations.recommend('1') == ([recipes.get_recipe('1')], 200)

	# If the user ID does not exist, the recommendation system should return an error message
	assert recommendations.recommend('2') == ({'error': 'User not found'}, 404)
