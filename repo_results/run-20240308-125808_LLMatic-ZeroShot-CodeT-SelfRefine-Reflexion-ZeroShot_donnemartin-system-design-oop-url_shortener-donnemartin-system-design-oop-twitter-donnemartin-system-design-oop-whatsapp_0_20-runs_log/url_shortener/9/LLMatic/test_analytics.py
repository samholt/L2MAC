import analytics
import datetime


def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	assert len(analytics.analytics_db['test_url']) == 1


def test_get_statistics():
	click_data = analytics.get_statistics('test_url')
	assert len(click_data) == 1
	assert isinstance(click_data[0]['time'], datetime.datetime)
	assert click_data[0]['ip_address'] == '8.8.8.8'
