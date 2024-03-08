import pytest
from review import Review

def test_write_review():
	user_id = 1
	recipe_id = 1
	review = 'Delicious!'
	my_review = Review(user_id, recipe_id, review)
	assert my_review.write_review() == review
