import analytics
import datetime

def test_track_click():
	analytics.track_click('test_url', '128.101.101.101')
	assert len(analytics.analytics_db['test_url']) == 1
	assert 'time' in analytics.analytics_db['test_url'][0]
	assert isinstance(analytics.analytics_db['test_url'][0]['time'], datetime.datetime)
	assert 'ip' in analytics.analytics_db['test_url'][0]
	assert analytics.analytics_db['test_url'][0]['ip'] == '128.101.101.101'
	assert 'location' in analytics.analytics_db['test_url'][0]

def test_get_statistics():
	stats = analytics.get_statistics('test_url')
	assert len(stats) == 1
	assert 'time' in stats[0]
	assert isinstance(stats[0]['time'], datetime.datetime)
	assert 'ip' in stats[0]
	assert stats[0]['ip'] == '128.101.101.101'
	assert 'location' in stats[0]
