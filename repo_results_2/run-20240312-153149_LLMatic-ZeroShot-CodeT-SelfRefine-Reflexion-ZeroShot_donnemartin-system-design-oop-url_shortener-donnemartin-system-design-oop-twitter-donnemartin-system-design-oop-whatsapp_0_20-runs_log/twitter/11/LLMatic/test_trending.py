import pytest
from trending import Trending

def test_get_trending_topics():
	trending = Trending()
	assert isinstance(trending.get_trending_topics(), dict)

def test_sort_trending_topics():
	trending = Trending()
	assert isinstance(trending.sort_trending_topics(), dict)
