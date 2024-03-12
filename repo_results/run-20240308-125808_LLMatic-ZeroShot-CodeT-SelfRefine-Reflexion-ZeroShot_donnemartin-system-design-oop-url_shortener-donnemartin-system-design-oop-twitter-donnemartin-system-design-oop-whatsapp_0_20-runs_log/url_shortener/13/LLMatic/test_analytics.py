import analytics


def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	assert len(analytics.analytics_db['test_url']) == 1


def test_get_statistics():
	stats = analytics.get_statistics('test_url')
	assert len(stats) == 1
