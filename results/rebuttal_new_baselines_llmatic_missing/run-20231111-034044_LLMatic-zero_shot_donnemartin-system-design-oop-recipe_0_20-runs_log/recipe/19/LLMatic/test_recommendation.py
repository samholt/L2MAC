import pytest
from recommendation import Recommendation

def test_generate_recommendations():
	rec = Recommendation()
	rec.user_preferences = {'user1': ['Italian', 'Mexican']}
	rec.user_activity = {'user1': ['recipe1', 'recipe2']}
	rec.recipe_database = {'recipe3': {'id': 'recipe3', 'category': 'Italian'}, 'recipe4': {'id': 'recipe4', 'category': 'Chinese'}}
	recommendations = rec.generate_recommendations('user1')
	assert len(recommendations) == 1
	assert recommendations[0]['id'] == 'recipe3'

def test_notify_user():
	rec = Recommendation()
	rec.user_preferences = {'user1': ['Italian', 'Mexican']}
	new_recipes = [{'id': 'recipe5', 'category': 'Italian'}, {'id': 'recipe6', 'category': 'Chinese'}]
	rec.notify_user('user1', new_recipes)
