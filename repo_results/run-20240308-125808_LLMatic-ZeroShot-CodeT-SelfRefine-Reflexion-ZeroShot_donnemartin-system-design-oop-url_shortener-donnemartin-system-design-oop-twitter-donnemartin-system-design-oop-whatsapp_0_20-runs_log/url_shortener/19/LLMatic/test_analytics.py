from analytics import Analytics


def test_track_url():
	analytics = Analytics()
	url = 'http://example.com'
	analytics.track_url(url)
	assert analytics.get_url_clicks(url) == 1
	assert len(analytics.get_url_details(url)) == 1

	analytics.track_url(url)
	assert analytics.get_url_clicks(url) == 2
	assert len(analytics.get_url_details(url)) == 2


def test_get_url_clicks():
	analytics = Analytics()
	url = 'http://example2.com'
	assert analytics.get_url_clicks(url) == 0

	analytics.track_url(url)
	assert analytics.get_url_clicks(url) == 1


def test_get_url_details():
	analytics = Analytics()
	url = 'http://example3.com'
	assert analytics.get_url_details(url) == []

	analytics.track_url(url)
	assert len(analytics.get_url_details(url)) == 1
