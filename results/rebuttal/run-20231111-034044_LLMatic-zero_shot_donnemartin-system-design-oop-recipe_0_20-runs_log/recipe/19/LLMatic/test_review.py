import pytest
from review import Review

def test_write_review():
	review = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review.write_review() == {'user': 'User1', 'recipe': 'Recipe1', 'rating': 5, 'text': 'Great recipe!'}

	review.delete_review()
	assert review.write_review() == 'Review has been deleted'

def test_delete_review():
	review = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review.delete_review() == 'Review has been deleted'
	assert review.deleted == True
