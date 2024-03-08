import pytest
from recommendation import Recommendation
from user import User
from recipe import Recipe


def test_generate_recommendations():
	user = User('test_user', 'test_password')
	user.set_preferences(['Italian', 'Mexican'])
	recipes = [Recipe('Pizza', [], '', [], 'Italian', '', 'Italian', ''), Recipe('Tacos', [], '', [], 'Mexican', '', 'Mexican', ''), Recipe('Sushi', [], '', [], 'Japanese', '', 'Japanese', '')]
	recommendation = Recommendation(user, recipes)
	recommended_recipes = recommendation.generate_recommendations()
	assert len(recommended_recipes) == 2
	assert recommended_recipes[0].name == 'Pizza'
	assert recommended_recipes[1].name == 'Tacos'


def test_notify_user():
	user = User('test_user', 'test_password')
	user.set_interest_areas(['Italian', 'Mexican'])
	new_recipes = [Recipe('Pasta', [], '', [], 'Italian', '', 'Italian', ''), Recipe('Burrito', [], '', [], 'Mexican', '', 'Mexican', ''), Recipe('Ramen', [], '', [], 'Japanese', '', 'Japanese', '')]
	recommendation = Recommendation(user, new_recipes)
	new_recipes_in_interest_areas = recommendation.notify_user(new_recipes)
	assert len(new_recipes_in_interest_areas) == 2
	assert new_recipes_in_interest_areas[0].name == 'Pasta'
	assert new_recipes_in_interest_areas[1].name == 'Burrito'
