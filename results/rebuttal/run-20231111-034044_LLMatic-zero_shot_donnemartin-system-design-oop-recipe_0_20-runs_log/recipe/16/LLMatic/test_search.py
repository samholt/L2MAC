import pytest
from search import Search

def test_search_by_ingredients():
	search = Search({'recipes': {
		1: {'ingredients': ['tomato', 'lettuce', 'bread'], 'name': 'Sandwich', 'category': 'Fast Food'},
		2: {'ingredients': ['pasta', 'tomato', 'cheese'], 'name': 'Pasta', 'category': 'Italian'}
	}})
	assert search.search_by_ingredients(['tomato', 'lettuce']) == [{'ingredients': ['tomato', 'lettuce', 'bread'], 'name': 'Sandwich', 'category': 'Fast Food'}]


def test_search_by_name():
	search = Search({'recipes': {
		1: {'ingredients': ['tomato', 'lettuce', 'bread'], 'name': 'Sandwich', 'category': 'Fast Food'},
		2: {'ingredients': ['pasta', 'tomato', 'cheese'], 'name': 'Pasta', 'category': 'Italian'}
	}})
	assert search.search_by_name('Sandwich') == [{'ingredients': ['tomato', 'lettuce', 'bread'], 'name': 'Sandwich', 'category': 'Fast Food'}]


def test_search_by_category():
	search = Search({'recipes': {
		1: {'ingredients': ['tomato', 'lettuce', 'bread'], 'name': 'Sandwich', 'category': 'Fast Food'},
		2: {'ingredients': ['pasta', 'tomato', 'cheese'], 'name': 'Pasta', 'category': 'Italian'}
	}})
	assert search.search_by_category('Italian') == [{'ingredients': ['pasta', 'tomato', 'cheese'], 'name': 'Pasta', 'category': 'Italian'}]
