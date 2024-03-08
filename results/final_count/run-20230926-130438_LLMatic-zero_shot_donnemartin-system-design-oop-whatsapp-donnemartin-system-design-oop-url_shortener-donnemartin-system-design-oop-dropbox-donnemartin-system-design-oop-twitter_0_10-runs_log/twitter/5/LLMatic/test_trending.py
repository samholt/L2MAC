import pytest
from trending import Trending

def test_get_trending_topics():
	trending = Trending()
	assert trending.get_trending_topics() == {}

def test_sort_trending_topics():
	trending = Trending()
	assert trending.sort_trending_topics() == {}
