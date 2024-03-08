import pytest
from recommendation import Recommendation
from user import User
from recipe import Recipe


def test_generate_recommendations():
	user = User('test_user', 'test_password')
	user.create_account('test_user', 'test_password', ['Italian', 'Mexican'])
	recipes = [Recipe('Spaghetti', 'Italian', 'test_instructions', 'test_user'), Recipe('Tacos', 'Mexican', 'test_instructions', 'test_user'), Recipe('Sushi', 'Japanese', 'test_instructions', 'test_user')]
	recommendation = Recommendation(user, recipes)
	recommended_recipes = recommendation.generate_recommendations()
	assert len(recommended_recipes) == 2
	assert recommended_recipes[0].name == 'Spaghetti'
	assert recommended_recipes[1].name == 'Tacos'


def test_notify_user():
	user = User('test_user', 'test_password')
	user.create_account('test_user', 'test_password', ['Italian', 'Mexican'])
	new_recipes = [Recipe('Pizza', 'Italian', 'test_instructions', 'test_user'), Recipe('Sushi', 'Japanese', 'test_instructions', 'test_user')]
	recommendation = Recommendation(user, new_recipes)
	message = recommendation.notify_user(new_recipes)
	assert message == 'You have new recipe recommendations in your interest areas!'
