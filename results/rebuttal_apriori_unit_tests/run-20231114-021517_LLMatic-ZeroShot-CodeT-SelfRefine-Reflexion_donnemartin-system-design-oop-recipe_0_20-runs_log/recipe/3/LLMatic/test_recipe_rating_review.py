import pytest
import random

from recipe_platform import RecipeRating, RecipeReview

def test_recipe_rating():
	recipe_id = random.randint(1, 1000)
	rating = random.randint(1, 5)
	RecipeRating().submit_rating(recipe_id, rating)
	assert RecipeRating().get_average_rating(recipe_id) >= 1

def test_recipe_review():
	recipe_id = random.randint(1, 1000)
	review = "Great recipe!"
	RecipeReview().submit_review(recipe_id, review)
	assert any(r == review for r in RecipeReview().get_reviews(recipe_id))

def test_display_average_rating():
	recipe_id = random.randint(1, 1000)
	average_rating = RecipeRating().get_average_rating(recipe_id)
	assert isinstance(average_rating, float) and 1 <= average_rating <= 5
