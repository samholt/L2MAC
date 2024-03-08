import pytest
from review import Review
from user import User
from recipe import Recipe

def test_review_class():
	user = User('Test User', 'password')
	recipe = Recipe('Test Recipe', [], '', [], '')
	review = Review(user, recipe)

	# Test rating
	review.rate_recipe(5)
	assert review.rating == 5

	# Test review text
	review.review_recipe('Delicious!')
	assert review.review_text == 'Delicious!'

	# Test average rating calculation
	reviews = [Review(user, recipe, rating) for rating in range(1, 6)]
	assert Review.calculate_average_rating(reviews) == 3.0
