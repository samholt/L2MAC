import pytest
from models import User, Recipe


def test_create_user():
	user = User(id=1, username='test', email='test@test.com')
	assert user.id == 1
	assert user.username == 'test'
	assert user.email == 'test@test.com'

def test_create_recipe():
	recipe = Recipe(id=1, title='test recipe', instructions='test instructions', user_id=1)
	assert recipe.id == 1
	assert recipe.title == 'test recipe'
	assert recipe.instructions == 'test instructions'
	assert recipe.user_id == 1
