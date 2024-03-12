import pytest
from trending import Trending

def test_trending():
	trending = Trending()
	trending.add_topic('topic1')
	trending.add_topic('topic2')
	trending.add_topic('topic1')
	assert trending.get_trending_topics() == [('topic1', 2), ('topic2', 1)]
	assert trending.sort_trending_topics() == [('topic1', 2), ('topic2', 1)]
	assert trending.sort_trending_topics('location1') == []
