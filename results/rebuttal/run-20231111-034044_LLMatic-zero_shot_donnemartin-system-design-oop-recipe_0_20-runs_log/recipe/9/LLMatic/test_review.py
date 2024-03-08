import pytest
from review import Review


def test_review_class():
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	assert review.user == 'user1'
	assert review.recipe == 'recipe1'
	assert review.rating == 5
	assert review.review_text == 'Great recipe!'

	review.write_review('Amazing recipe!')
	assert review.review_text == 'Amazing recipe!'

	review.rate_recipe(4)
	assert review.rating == 4
