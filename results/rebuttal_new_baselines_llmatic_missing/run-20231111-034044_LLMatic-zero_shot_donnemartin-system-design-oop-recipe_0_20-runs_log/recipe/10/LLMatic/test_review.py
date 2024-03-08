import pytest
from user import User
from recipe import Recipe
from review import Review

def test_review_creation():
	user = User('test_user', 'password')
	review = Review(user, 5, 'Great recipe!')
	assert review.user == user
	assert review.rating == 5
	assert review.review_text == 'Great recipe!'

def test_recipe_rating():
	user = User('test_user', 'password')
	recipe = Recipe('test_recipe', 'ingredients', 'instructions', 'images', 'categories')
	user.rate_recipe(recipe, 5, 'Great recipe!')
	assert len(recipe.reviews) == 1
	assert recipe.reviews[0].rating == 5
	assert recipe.reviews[0].review_text == 'Great recipe!'
	assert recipe.average_rating() == 5

