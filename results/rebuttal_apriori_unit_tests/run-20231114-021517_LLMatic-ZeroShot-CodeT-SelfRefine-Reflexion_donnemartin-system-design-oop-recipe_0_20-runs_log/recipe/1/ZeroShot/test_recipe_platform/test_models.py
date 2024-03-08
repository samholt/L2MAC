import pytest
import random
import string

from recipe_platform.models import User, Recipe, Rating, Review, Admin


def test_user_creation():
	user = User.create('user1', 'pass1')
	assert user.username == 'user1'
	assert user.password == 'pass1'


def test_recipe_creation():
	recipe = Recipe.create('recipe1', ['ingredient1'], 'instructions1', 'image1')
	assert recipe.title == 'recipe1'
	assert recipe.ingredients == ['ingredient1']
	assert recipe.instructions == 'instructions1'
	assert recipe.image == 'image1'


def test_rating_submission():
	Rating.submit_rating(1, 5)
	assert Rating.get_average_rating(1) == 5


def test_review_submission():
	Review.submit_review(1, 'Great recipe!')
	assert Review.get_reviews(1)[0].text == 'Great recipe!'


def test_admin_functions():
	admin = Admin.create('admin1', 'pass1')
	admin.edit_recipe(1, {'title': 'new title'})
	recipe = Recipe.get_by_id(1)
	assert recipe.title == 'new title'
	admin.remove_recipe(1)
	assert Recipe.get_by_id(1) is None
	stats = admin.get_site_statistics()
	assert 'total_users' in stats
	assert 'total_recipes' in stats
