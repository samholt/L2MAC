import pytest
from search import Search

def test_search_by_ingredient():
	search = Search({'1': {'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}, '2': {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'}})
	assert search.search_by_ingredient('tomato') == [{'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}, {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'}]

def test_search_by_name():
	search = Search({'1': {'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}, '2': {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'}})
	assert search.search_by_name('pasta') == [{'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}]

def test_search_by_category():
	search = Search({'1': {'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}, '2': {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'}})
	assert search.search_by_category('italian') == [{'name': 'Pasta', 'ingredients': ['pasta', 'tomato', 'cheese'], 'category': 'Italian'}, {'name': 'Pizza', 'ingredients': ['dough', 'tomato', 'cheese'], 'category': 'Italian'}]
