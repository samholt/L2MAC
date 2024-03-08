import pytest
from review import Review


def test_submit_review():
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	assert review.submit_review() == 'Review submitted successfully'

	review = Review('', 'recipe1', 5, 'Great recipe!')
	assert review.submit_review() == 'Review submission failed'
