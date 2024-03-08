import trending


def test_trending():
	t = trending.Trending()
	t.add_mention('topic1')
	t.add_mention('topic2')
	t.add_mention('topic1')
	t.add_mention('topic1', 'location1')
	assert t.get_trending() == [('topic1', 3), ('topic2', 1)]
	assert t.get_trending('location1') == [('topic1', 1)]
