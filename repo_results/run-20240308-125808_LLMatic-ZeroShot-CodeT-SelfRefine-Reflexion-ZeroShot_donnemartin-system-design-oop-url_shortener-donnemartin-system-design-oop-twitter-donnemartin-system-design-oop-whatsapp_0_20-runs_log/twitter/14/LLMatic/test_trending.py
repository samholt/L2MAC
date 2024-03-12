import pytest
from trending import Trending


def test_trending():
	trending = Trending()
	trending.add_topic('Python')
	trending.add_topic('Python')
	trending.add_topic('AI')
	assert trending.get_trending_topics() == [('Python', 2), ('AI', 1)]

	trending.add_topic('AI')
	assert trending.get_trending_topics() == [('Python', 2), ('AI', 2)]

	trending.add_topic('AI', 'USA')
	assert trending.sort_trending_topics('USA') == [('AI', 1)]
