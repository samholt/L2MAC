import analytics
import datetime

def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	assert len(analytics.analytics_db['test_url']) == 1
	assert 'timestamp' in analytics.analytics_db['test_url'][0]
	assert 'ip_address' in analytics.analytics_db['test_url'][0]

def test_get_statistics():
	analytics.track_click('test_url', '8.8.8.8')
	stats = analytics.get_statistics('test_url')
	assert len(stats) == 2
	assert 'timestamp' in stats[0]
	assert 'ip_address' in stats[0]
