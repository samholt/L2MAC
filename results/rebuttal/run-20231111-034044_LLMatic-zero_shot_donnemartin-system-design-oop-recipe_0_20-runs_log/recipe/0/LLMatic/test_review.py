import pytest
from review import Review


def test_create_review():
	id = '1'
	user = 'test_user'
	rating = 5
	content = 'Great recipe!'
	review = Review.create_review(id, user, rating, content)
	assert review.id == id
	assert review.user == user
	assert review.rating == rating
	assert review.content == content


def test_calculate_average_rating():
	reviews = [Review('1', 'User1', 5, 'Great!'), Review('2', 'User2', 4, 'Good'), Review('3', 'User3', 3, 'Okay')]
	assert Review.calculate_average_rating(reviews) == 4
