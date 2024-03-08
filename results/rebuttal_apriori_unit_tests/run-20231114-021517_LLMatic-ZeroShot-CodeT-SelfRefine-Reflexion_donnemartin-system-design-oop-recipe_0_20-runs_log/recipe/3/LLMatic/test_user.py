import pytest
import random
import string

from recipe_platform import User

def test_account_creation_management():
	user_data = {'username': 'user123', 'password': 'pass123'}
	user = User.create(**user_data)
	assert user.is_valid()

	user.change_password('newpass123')
	assert user.password == 'newpass123'

def test_save_favorite_recipes():
	user = User.get_by_username('user123')
	recipe_id = random.randint(1, 1000)
	user.save_favorite(recipe_id)
	assert recipe_id in user.favorites

def test_profile_page_content():
	user = User.get_by_username('user123')
	assert hasattr(user, 'submitted_recipes')
	assert hasattr(user, 'favorites')
