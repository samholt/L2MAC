import pytest
from search import Search

def test_search_by_keyword():
	search = Search(['Hello world', 'Python is cool', 'I love programming'])
	assert search.search_by_keyword('Python') == ['Python is cool']


def test_filter_by_hashtag():
	search = Search(['#Hello world', 'Python is #cool', 'I love #programming'])
	assert search.filter_by_hashtag('cool') == ['Python is #cool']


def test_filter_by_user_mention():
	search = Search(['@John Hello world', 'Python is cool', 'I love programming'])
	assert search.filter_by_user_mention('John') == ['@John Hello world']


def test_filter_by_trending():
	search = Search(['#Hello world', 'Python is #cool', 'I love #programming'])
	assert search.filter_by_trending(['Hello', 'cool']) == ['#Hello world', 'Python is #cool']
