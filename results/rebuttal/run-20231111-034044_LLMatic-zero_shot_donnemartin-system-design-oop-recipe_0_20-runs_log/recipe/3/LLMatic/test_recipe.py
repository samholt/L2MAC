import pytest
from recipe import Recipe
from review import Review


def test_add_review():
	recipe = Recipe('Spaghetti', 'Italian', 'test_instructions', 'test_user')
	review = Review('test_user', 'Spaghetti', 5, 'Delicious!')
	recipe.add_review(review)
	assert len(recipe.reviews) == 1
	assert recipe.reviews[0].rating == 5
	assert recipe.reviews[0].text == 'Delicious!'


def test_get_average_rating():
	recipe = Recipe('Spaghetti', 'Italian', 'test_instructions', 'test_user')
	review1 = Review('test_user1', 'Spaghetti', 5, 'Delicious!')
	review2 = Review('test_user2', 'Spaghetti', 4, 'Pretty good')
	recipe.add_review(review1)
	recipe.add_review(review2)
	assert recipe.get_average_rating() == 4.5
