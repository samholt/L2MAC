import pytest
from trending import Trending

def test_get_trending_topics():
	trending = Trending()
	topics = ['topic1', 'topic2', 'topic3', 'topic1', 'topic2', 'topic1']
	for topic in topics:
		trending.add_topic(topic)
	assert trending.get_trending_topics() == ['topic1', 'topic2', 'topic3']
