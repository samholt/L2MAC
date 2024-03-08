import analytics
import datetime


def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	assert len(analytics.ANALYTICS_DB['test_url']) == 1
	assert isinstance(analytics.ANALYTICS_DB['test_url'][0]['time'], datetime.datetime)
	assert isinstance(analytics.ANALYTICS_DB['test_url'][0]['location'], str)


def test_get_analytics():
	analytics_data = analytics.get_analytics('test_url')
	assert len(analytics_data) == 1
	assert isinstance(analytics_data[0]['time'], datetime.datetime)
	assert isinstance(analytics_data[0]['location'], str)
