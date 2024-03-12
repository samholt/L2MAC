import analytics
import datetime

def test_record_click():
	analytics.analytics_db = {}
	analytics.record_click('test', '128.101.101.101')
	assert len(analytics.analytics_db['test']) == 1
	assert isinstance(analytics.analytics_db['test'][0]['date_time'], datetime.datetime)
	assert isinstance(analytics.analytics_db['test'][0]['ip'], str)

def test_get_analytics():
	analytics.analytics_db = {}
	analytics.record_click('test', '128.101.101.101')
	analytics_data = analytics.get_analytics('test')
	assert len(analytics_data) == 1
	assert isinstance(analytics_data[0]['date_time'], datetime.datetime)
	assert isinstance(analytics_data[0]['ip'], str)
