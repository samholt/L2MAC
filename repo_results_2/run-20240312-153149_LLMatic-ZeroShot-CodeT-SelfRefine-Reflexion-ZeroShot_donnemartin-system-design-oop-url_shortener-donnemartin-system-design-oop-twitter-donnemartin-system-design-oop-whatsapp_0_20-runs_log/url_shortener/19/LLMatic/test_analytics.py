import analytics


def test_track_click():
	short_url = 'abc123'
	analytics.track_click(short_url)
	stats = analytics.get_statistics(short_url)

	assert len(stats) == 1
	assert 'timestamp' in stats[0]
	assert 'location' in stats[0]


def test_get_statistics():
	short_url = 'def456'
	stats = analytics.get_statistics(short_url)

	assert stats == []
