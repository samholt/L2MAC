import analytics


def test_track_click():
	an = analytics.Analytics()
	an.track_click('abc123', 'USA')
	data = an.get_click_data('abc123')
	assert len(data) == 1
	assert data[0]['location'] == 'USA'


def test_get_click_data():
	an = analytics.Analytics()
	data = an.get_click_data('abc123')
	assert data == []
