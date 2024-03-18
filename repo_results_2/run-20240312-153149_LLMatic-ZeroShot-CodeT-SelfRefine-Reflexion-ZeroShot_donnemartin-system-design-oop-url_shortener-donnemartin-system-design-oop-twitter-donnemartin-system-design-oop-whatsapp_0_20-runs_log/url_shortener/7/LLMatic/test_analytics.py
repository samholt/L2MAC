import analytics
import datetime

def test_track_click():
	analytics_obj = analytics.Analytics()
	analytics_obj.track_click('abc123', '8.8.8.8')
	assert len(analytics_obj.ANALYTICS_DB['abc123']) == 1
	assert 'date_time' in analytics_obj.ANALYTICS_DB['abc123'][0]
	assert 'ip_address' in analytics_obj.ANALYTICS_DB['abc123'][0]

	analytics_obj.track_click('abc123', '8.8.4.4')
	assert len(analytics_obj.ANALYTICS_DB['abc123']) == 2

	analytics_obj.track_click('def456', '8.8.8.8')
	assert len(analytics_obj.ANALYTICS_DB['def456']) == 1


def test_get_analytics():
	analytics_obj = analytics.Analytics()
	analytics_obj.ANALYTICS_DB = {}
	analytics_obj.track_click('abc123', '8.8.8.8')
	analytics_obj.track_click('abc123', '8.8.4.4')
	analytics_obj.track_click('def456', '8.8.8.8')

	abc123_analytics = analytics_obj.get_analytics('abc123')
	assert len(abc123_analytics) == 2
	assert abc123_analytics[0]['date_time'].date() == datetime.datetime.now().date()
	assert abc123_analytics[0]['ip_address'] is not None

	def456_analytics = analytics_obj.get_analytics('def456')
	assert len(def456_analytics) == 1
	assert def456_analytics[0]['date_time'].date() == datetime.datetime.now().date()
	assert def456_analytics[0]['ip_address'] is not None

	no_analytics = analytics_obj.get_analytics('ghi789')
	assert len(no_analytics) == 0
