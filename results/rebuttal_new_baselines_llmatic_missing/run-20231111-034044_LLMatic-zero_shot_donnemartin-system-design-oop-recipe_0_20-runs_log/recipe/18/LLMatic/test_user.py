import pytest
from user import User
from recipe import Recipe


def test_user_creation():
	user = User('test_user', 'password')
	assert user.username == 'test_user'
	assert user.password == 'password'


def test_save_favorite_recipe():
	user = User('test_user', 'password')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])
	user.save_favorite_recipe(recipe)
	assert recipe in user.favorite_recipes


def test_submit_recipe():
	user = User('test_user', 'password')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])
	user.submit_recipe(recipe)
	assert recipe in user.submitted_recipes


def test_follow_user():
	user1 = User('test_user1', 'password')
	user2 = User('test_user2', 'password')
	user1.follow_user(user2)
	assert user2 in user1.followed_users


def test_view_feed():
	user1 = User('test_user1', 'password')
	user2 = User('test_user2', 'password')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])
	user2.submit_recipe(recipe)
	user1.follow_user(user2)
	assert recipe in user1.view_feed()


def test_generate_recommendations():
	user = User('test_user', 'password')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])
	user.save_favorite_recipe(recipe)
	user.generate_recommendations()
	assert recipe in user.recommendations


def test_receive_notifications():
	user = User('test_user', 'password')
	recipe = Recipe('new_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])
	user.receive_notifications(recipe)
	assert recipe in user.notifications
