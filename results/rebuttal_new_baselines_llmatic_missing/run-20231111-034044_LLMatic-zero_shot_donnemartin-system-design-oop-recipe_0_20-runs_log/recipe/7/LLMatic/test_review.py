import pytest
from review import Review

def test_review_creation():
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	assert review.user == 'user1'
	assert review.recipe == 'recipe1'
	assert review.rating == 5
	assert review.review_text == 'Great recipe!'

def test_calculate_average_rating():
	reviews = [
		Review('user1', 'recipe1', 5, 'Great recipe!'),
		Review('user2', 'recipe1', 4, 'Good recipe!'),
		Review('user3', 'recipe1', 3, 'Average recipe!')
	]
	assert Review.calculate_average_rating(reviews) == 4
