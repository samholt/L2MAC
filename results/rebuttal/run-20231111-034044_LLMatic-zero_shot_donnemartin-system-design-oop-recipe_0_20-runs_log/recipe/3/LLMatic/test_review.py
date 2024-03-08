import pytest
from review import Review

def test_review_initialization():
	review = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review.user == 'User1'
	assert review.recipe == 'Recipe1'
	assert review.rating == 5
	assert review.text == 'Great recipe!'

def test_write_review():
	review = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review.write_review() == {'user': 'User1', 'recipe': 'Recipe1', 'rating': 5, 'text': 'Great recipe!'}
