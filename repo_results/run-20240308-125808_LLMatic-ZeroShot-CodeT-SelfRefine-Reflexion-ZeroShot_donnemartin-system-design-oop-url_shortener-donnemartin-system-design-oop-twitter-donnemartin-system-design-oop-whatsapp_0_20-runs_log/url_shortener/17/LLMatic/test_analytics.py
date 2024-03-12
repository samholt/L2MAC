import analytics


def test_track_click():
	short_url = 'abc123'
	location = 'USA'
	analytics.track_click(short_url, location)
	click_data = analytics.get_click_data(short_url)
	assert len(click_data) == 1
	assert click_data[0]['location'] == location


def test_get_click_data():
	short_url = 'xyz789'
	click_data = analytics.get_click_data(short_url)
	assert click_data == []
