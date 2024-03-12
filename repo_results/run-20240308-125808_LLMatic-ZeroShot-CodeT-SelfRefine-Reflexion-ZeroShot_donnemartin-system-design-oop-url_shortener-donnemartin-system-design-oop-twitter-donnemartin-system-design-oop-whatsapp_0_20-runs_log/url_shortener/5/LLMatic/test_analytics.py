from analytics import Analytics


def test_analytics():
	analytics = Analytics()
	analytics.track_click('abc123', 'USA')
	analytics.track_click('abc123', 'Canada')
	stats = analytics.get_statistics('abc123')
	assert len(stats) == 2
	assert stats[0]['location'] == 'USA'
	assert stats[1]['location'] == 'Canada'
