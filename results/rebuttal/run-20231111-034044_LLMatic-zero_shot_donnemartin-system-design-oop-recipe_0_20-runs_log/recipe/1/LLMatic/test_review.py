import pytest
from review import Review


def test_submit_review():
	Review.review_db = {}
	review1 = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review1.submit_review() == 'Review submitted successfully'
	assert Review.review_db == {('User1', 'Recipe1'): review1}


def test_validate_review():
	review1 = Review('User1', 'Recipe1', 5, 'Great recipe!')
	assert review1.validate_review() == True
	review2 = Review('', 'Recipe1', 5, 'Great recipe!')
	assert review2.validate_review() == False
	review3 = Review('User1', 'Recipe1', 6, 'Great recipe!')
	assert review3.validate_review() == False


def test_get_reviews_for_recipe():
	Review.review_db = {}
	review1 = Review('User1', 'Recipe1', 5, 'Great recipe!')
	review1.submit_review()
	review2 = Review('User2', 'Recipe1', 4, 'Good recipe!')
	review2.submit_review()
	review3 = Review('User3', 'Recipe2', 5, 'Excellent recipe!')
	review3.submit_review()
	assert Review.get_reviews_for_recipe('Recipe1') == [review1, review2]
	assert Review.get_reviews_for_recipe('Recipe2') == [review3]
