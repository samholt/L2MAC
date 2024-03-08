import pytest
from recommendations import Recommendations
from users import UserManager, User
from recipes import Recipe

@pytest.fixture
def setup_data():
	user_manager = UserManager()
	recipe_manager = Recipe()
	user_manager.create_user('user1', 'password1')
	user_manager.create_user('user2', 'password2')
	user_manager.follow_user('user1', 'user2')
	recipe_manager.submit_recipe('recipe1', {'title': 'Recipe 1', 'ingredients': ['ingredient1', 'ingredient2'], 'instructions': 'Instructions'})
	user2 = user_manager.get_user('user2')
	user2.submitted_recipes.append('recipe1')
	return user_manager, recipe_manager


def test_generate_recommendations(setup_data):
	user_manager, recipe_manager = setup_data
	recommendations = Recommendations(user_manager, recipe_manager)
	assert recommendations.generate_recommendations('user1') == ['recipe1']


def test_send_notifications(setup_data):
	user_manager, recipe_manager = setup_data
	recommendations = Recommendations(user_manager, recipe_manager)
	assert recommendations.send_notifications('user1', ['recipe1']) == ['New recipe recipe1 from user2']
