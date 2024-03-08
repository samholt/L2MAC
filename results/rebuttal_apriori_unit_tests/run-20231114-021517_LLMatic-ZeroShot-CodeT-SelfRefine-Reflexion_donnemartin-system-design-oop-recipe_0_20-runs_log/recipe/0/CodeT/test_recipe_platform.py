import pytest
import random
import string

from recipe_platform.models import User, Recipe, Rating, Review, Admin

@pytest.fixture
def user():
	return User.create(id=1, username='user1', password='pass1')

@pytest.fixture
def recipe():
	return Recipe.create(id=1, title='recipe1', ingredients=['ingredient1'], instructions='instructions1', image='image1')

@pytest.fixture
def rating():
	return Rating.create(id=1, recipe_id=1, rating=5)

@pytest.fixture
def review():
	return Review.create(id=1, recipe_id=1, review='review1')

@pytest.fixture
def admin():
	return Admin.create(id=1, username='admin1', password='pass1')


def test_user_creation(user):
	assert user.id == 1
	assert user.username == 'user1'
	assert user.password == 'pass1'


def test_recipe_creation(recipe):
	assert recipe.id == 1
	assert recipe.title == 'recipe1'
	assert recipe.ingredients == ['ingredient1']
	assert recipe.instructions == 'instructions1'
	assert recipe.image == 'image1'


def test_rating_creation(rating):
	assert rating.id == 1
	assert rating.recipe_id == 1
	assert rating.rating == 5


def test_review_creation(review):
	assert review.id == 1
	assert review.recipe_id == 1
	assert review.review == 'review1'


def test_admin_creation(admin):
	assert admin.id == 1
	assert admin.username == 'admin1'
	assert admin.password == 'pass1'

