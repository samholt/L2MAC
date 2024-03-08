import pytest
from rating import Rating

def test_rating_initialization():
	user = 'test_user'
	recipe = 'test_recipe'
	rating = 5
	review = 'Great recipe!'
	r = Rating(user, recipe, rating, review)
	assert r.user == user
	assert r.recipe == recipe
	assert r.rating == rating
	assert r.review == review

def test_rate_recipe():
	r = Rating('test_user', 'test_recipe', 5, 'Great recipe!')
	r.rate_recipe(4)
	assert r.rating == 4

def test_write_review():
	r = Rating('test_user', 'test_recipe', 5, 'Great recipe!')
	r.write_review('Good recipe!')
	assert r.review == 'Good recipe!'

def test_calculate_average_rating():
	ratings = [5, 4, 3, 2, 1]
	assert Rating.calculate_average_rating(ratings) == 3
