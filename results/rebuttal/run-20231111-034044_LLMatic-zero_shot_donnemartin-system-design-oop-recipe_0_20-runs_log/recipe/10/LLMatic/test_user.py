import pytest
from user import User
from recipe import Recipe

def test_user_creation():
	user = User('testuser', 'password')
	assert user.username == 'testuser'
	assert user.password == 'password'


def test_submit_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	assert user.submit_recipe(recipe) == True


def test_edit_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	user.submit_recipe(recipe)
	assert user.edit_recipe(recipe, 'new name', 'new ingredients', 'new instructions', 'new images', 'new categories') == True


def test_delete_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	user.submit_recipe(recipe)
	assert user.delete_recipe(recipe) == False


def test_save_favorite_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	user.save_favorite_recipe(recipe)
	assert recipe in user.favorite_recipes


def test_rate_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	user.rate_recipe(recipe, 5, 'Great recipe!')
	assert len(recipe.reviews) == 1


def test_follow_user():
	user1 = User('testuser1', 'password')
	user2 = User('testuser2', 'password')
	user1.follow_user(user2)
	assert user2 in user1.following


def test_unfollow_user():
	user1 = User('testuser1', 'password')
	user2 = User('testuser2', 'password')
	user1.follow_user(user2)
	user1.unfollow_user(user2)
	assert user2 not in user1.following


def test_update_feed():
	user1 = User('testuser1', 'password')
	user2 = User('testuser2', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	user2.submit_recipe(recipe)
	user1.follow_user(user2)
	user1.update_feed()
	assert recipe in user1.feed


def test_share_recipe():
	user = User('testuser', 'password')
	recipe = Recipe('test recipe', 'ingredients', 'instructions', 'images', 'categories')
	assert user.share_recipe(recipe, 'Facebook') == 'Shared test recipe on Facebook!'


def test_get_recommendations():
	user = User('testuser', 'password')
	recipe1 = Recipe('test recipe1', 'ingredients', 'instructions', 'images', ['category1'])
	recipe2 = Recipe('test recipe2', 'ingredients', 'instructions', 'images', ['category2'])
	all_recipes = [recipe1, recipe2]
	user.save_favorite_recipe(recipe1)
	recommendations = user.get_recommendations(all_recipes)
	assert recipe1 in recommendations


def test_receive_notifications():
	user = User('testuser', 'password')
	recipe1 = Recipe('test recipe1', 'ingredients', 'instructions', 'images', ['category1'])
	recipe2 = Recipe('test recipe2', 'ingredients', 'instructions', 'images', ['category2'])
	new_recipes = [recipe1, recipe2]
	user.save_favorite_recipe(recipe1)
	user.receive_notifications(new_recipes)
	assert 'New recipe: test recipe1' in user.notifications

