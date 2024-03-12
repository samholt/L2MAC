import analytics
import datetime


def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	click_data = analytics.get_analytics('test_url')
	assert len(click_data) == 1
	assert isinstance(click_data[0]['time'], datetime.datetime)
	assert 'ip_address' in click_data[0]


def test_get_analytics():
	click_data = analytics.get_analytics('test_url')
	assert len(click_data) == 1
	assert isinstance(click_data[0]['time'], datetime.datetime)
	assert 'ip_address' in click_data[0]
