import pytest
from reviews import Review

def test_add_and_get_review():
	review = Review()
	review.add_review('user1', 'recipe1', 5, 'Great recipe!')
	reviews = review.get_reviews('recipe1')
	assert len(reviews) == 1
	assert reviews[0]['user_id'] == 'user1'
	assert reviews[0]['rating'] == 5
	assert reviews[0]['review'] == 'Great recipe!'

def test_get_average_rating():
	review = Review()
	review.add_review('user1', 'recipe1', 5, 'Great recipe!')
	review.add_review('user2', 'recipe1', 4, 'Good recipe.')
	average_rating = review.get_average_rating('recipe1')
	assert average_rating == 4.5
