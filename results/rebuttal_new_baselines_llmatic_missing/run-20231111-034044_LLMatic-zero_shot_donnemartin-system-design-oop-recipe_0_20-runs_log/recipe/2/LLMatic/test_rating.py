import pytest
from rating import Rating


def test_rating_initialization():
	user = 'test_user'
	recipe = 'test_recipe'
	rating_value = 5
	review = 'Great recipe!'
	rating = Rating(user, recipe, rating_value, review)

	assert rating.user == user
	assert rating.recipe == recipe
	assert rating.rating == rating_value
	assert rating.review == review


def test_calculate_average_rating():
	ratings = [
		Rating('user1', 'recipe1', 5, 'review1'),
		Rating('user2', 'recipe2', 4, 'review2'),
		Rating('user3', 'recipe3', 3, 'review3')
	]

	average_rating = Rating.calculate_average_rating(ratings)
	assert average_rating == 4
