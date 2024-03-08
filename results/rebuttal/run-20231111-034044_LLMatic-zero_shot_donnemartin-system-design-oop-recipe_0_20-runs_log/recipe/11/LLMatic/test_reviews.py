import pytest
from reviews import Review
from database import MockDatabase

def test_add_review():
	db = MockDatabase()
	review = Review(db)
	response = review.add_review('user1', 'recipe1', 5, 'Great recipe!')
	assert response['status'] == 'success'

def test_get_reviews():
	db = MockDatabase()
	review = Review(db)
	review.add_review('user1', 'recipe1', 5, 'Great recipe!')
	response = review.get_reviews('recipe1')
	assert response['status'] == 'success'
	assert len(response['data']) == 1

def test_delete_review():
	db = MockDatabase()
	review = Review(db)
	review.add_review('user1', 'recipe1', 5, 'Great recipe!')
	response = review.delete_review('user1', 'recipe1')
	assert response['status'] == 'success'
