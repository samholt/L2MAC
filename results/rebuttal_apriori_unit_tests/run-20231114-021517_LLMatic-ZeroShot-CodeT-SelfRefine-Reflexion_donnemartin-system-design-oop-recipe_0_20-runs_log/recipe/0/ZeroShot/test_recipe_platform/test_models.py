import pytest
from recipe_platform.models import User, Admin, Recipe, RecipeRating, RecipeReview, RecipeSharing


def test_user():
	user = User(id=1, username='user1', password='pass1', favorites=[], submitted_recipes=[], following=[])
	assert user.username == 'user1'


def test_admin():
	admin = Admin(id=1, username='admin1', password='pass1', favorites=[], submitted_recipes=[], following=[])
	assert admin.username == 'admin1'


def test_recipe():
	recipe = Recipe(id=1, title='recipe1', ingredients=['ingredient1'], instructions='instructions1', image='image1', categories=['category1'])
	assert recipe.title == 'recipe1'


def test_recipe_rating():
	rating = RecipeRating(recipe_id=1, rating=5)
	assert rating.rating == 5


def test_recipe_review():
	review = RecipeReview(recipe_id=1, review='review1')
	assert review.review == 'review1'


def test_recipe_sharing():
	sharing = RecipeSharing(recipe_id=1, platform='platform1')
	assert sharing.platform == 'platform1'
