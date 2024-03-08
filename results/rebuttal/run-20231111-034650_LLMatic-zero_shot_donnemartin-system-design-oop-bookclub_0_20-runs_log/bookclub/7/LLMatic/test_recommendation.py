import pytest
from recommendation import Recommendation

def test_recommendation():
	rec = Recommendation()
	rec.recommend_book('user1', 'book1')
	rec.recommend_book('user1', 'book2')
	rec.recommend_book('user2', 'book1')
	assert rec.get_recommendations('user1') == ['book1', 'book2']
	assert rec.get_recommendations('user2') == ['book1']

	rec.highlight_popular_book('book1')
	rec.highlight_popular_book('book1')
	rec.highlight_popular_book('book2')
	assert rec.get_popular_books() == [('book1', 2), ('book2', 1)]
