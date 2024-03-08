import pytest
from recommendation import Recommendation


def test_generate_recommendations():
	user = 'test_user'
	recipes = ['recipe1', 'recipe2', 'recipe3', 'recipe4', 'recipe5', 'recipe6']
	recommendation = Recommendation(user, recipes)
	recommended_recipes = recommendation.generate_recommendations()
	assert len(recommended_recipes) == 5
	for recipe in recommended_recipes:
		assert recipe in recipes


def test_notify_user():
	user = 'test_user'
	new_recipes = ['new_recipe1', 'new_recipe2']
	recommendation = Recommendation(user, [])
	recommendation.notify_user(new_recipes)

