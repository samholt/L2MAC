import trending

def test_get_trending_topics():
	topics = trending.get_trending_topics()
	assert len(topics) == 5
	assert all(isinstance(topic, str) for topic in topics)


def test_sort_trending_topics():
	topics = trending.sort_trending_topics('location1')
	assert len(topics) == 10
	assert all(isinstance(topic, str) for topic in topics)
