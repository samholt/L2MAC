import pytest
from review import Review

def test_write_review():
	user = 'test_user'
	recipe = 'test_recipe'
	review = Review(user, recipe, 'Good recipe')
	assert review.write_review('Great recipe') == 'Review updated successfully.'
	assert review.review == 'Great recipe'
