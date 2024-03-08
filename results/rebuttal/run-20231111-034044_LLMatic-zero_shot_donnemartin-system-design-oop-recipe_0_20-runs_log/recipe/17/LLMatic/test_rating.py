import pytest
from rating import Rating

def test_rate_recipe():
	user_id = 1
	recipe_id = 1
	rating = 5
	my_rating = Rating(user_id, recipe_id, rating)
	assert my_rating.rate_recipe() == rating
