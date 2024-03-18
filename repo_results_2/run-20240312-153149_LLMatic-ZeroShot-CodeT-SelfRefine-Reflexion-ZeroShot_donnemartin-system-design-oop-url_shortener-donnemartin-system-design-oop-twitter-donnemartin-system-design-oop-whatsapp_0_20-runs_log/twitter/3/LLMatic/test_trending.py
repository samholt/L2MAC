import pytest
from trending import Trending

def test_trending():
	trending = Trending()
	topics = ['topic1', 'topic2', 'topic1', 'topic3', 'topic2', 'topic2', 'topic1', 'topic4']
	for topic in topics:
		trending.add_topic(topic)
	assert trending.get_trending_topics() == [('topic1', 3), ('topic2', 3), ('topic3', 1), ('topic4', 1)]
	assert trending.sort_trending_topics() == [('topic1', 3), ('topic2', 3), ('topic3', 1), ('topic4', 1)]
	assert trending.sort_trending_topics('unknown_location') == []
