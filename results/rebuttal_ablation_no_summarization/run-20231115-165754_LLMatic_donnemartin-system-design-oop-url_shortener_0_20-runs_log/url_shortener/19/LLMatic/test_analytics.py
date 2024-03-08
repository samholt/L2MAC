import analytics
import datetime


def test_track_click():
	analytics.analytics_db = {}
	analytics.track_click('testurl', '8.8.8.8')
	assert len(analytics.analytics_db['testurl']) == 1
	assert 'time' in analytics.analytics_db['testurl'][0]
	assert 'location' in analytics.analytics_db['testurl'][0]


def test_get_analytics():
	analytics.analytics_db = {
		'testurl': [
			{
				'time': datetime.datetime.now(),
				'location': 'USA'
			}
		]
	}
	data = analytics.get_analytics('testurl')
	assert len(data) == 1
	assert data[0]['location'] == 'USA'
