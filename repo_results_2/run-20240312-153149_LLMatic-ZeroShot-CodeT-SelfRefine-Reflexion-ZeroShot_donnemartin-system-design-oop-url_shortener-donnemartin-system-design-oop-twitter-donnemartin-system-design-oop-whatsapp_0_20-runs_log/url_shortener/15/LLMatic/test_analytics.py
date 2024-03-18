import analytics


def test_track_click():
	analytics.track_click('abc123', 'USA')
	assert len(analytics.analytics_db['abc123']) == 1
	assert analytics.analytics_db['abc123'][0]['location'] == 'USA'


def test_get_statistics():
	stats = analytics.get_statistics('abc123')
	assert stats['clicks'] == 1
	assert stats['details'][0]['location'] == 'USA'
