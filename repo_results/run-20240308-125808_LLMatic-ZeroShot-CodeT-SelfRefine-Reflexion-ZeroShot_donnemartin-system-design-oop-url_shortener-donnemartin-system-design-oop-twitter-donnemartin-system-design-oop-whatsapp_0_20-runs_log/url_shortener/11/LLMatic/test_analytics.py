import analytics


def test_track_click():
	short_url = 'abc123'
	location = 'USA'
	analytics.track_click(short_url, location)
	assert len(analytics.analytics_data[short_url]) == 1
	assert analytics.analytics_data[short_url][0]['location'] == location


def test_get_analytics():
	short_url = 'abc123'
	analytics_data = analytics.get_analytics(short_url)
	assert len(analytics_data) == 1
	assert analytics_data[0]['location'] == 'USA'
