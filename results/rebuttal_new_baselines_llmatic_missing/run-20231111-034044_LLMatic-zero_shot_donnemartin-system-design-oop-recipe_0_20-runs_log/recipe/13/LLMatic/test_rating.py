import pytest
from rating import Rating

def test_rate_recipe():
	user = 'test_user'
	recipe = 'test_recipe'
	rating = Rating(user, recipe, 3)
	assert rating.rate_recipe(5) == 'Rating updated successfully.'
	assert rating.rate_recipe(6) == 'Invalid rating. Please rate between 1 and 5.'
	assert rating.rating == 5
