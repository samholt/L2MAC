import analytics
import datetime


def test_get_url_stats():
	analytics.url_data = {'test': {'clicks': [{'time': '2022-01-01T00:00:00', 'location': 'USA'}]}}

	result = analytics.get_url_stats('test')
	assert result == {'clicks': 1, 'click_info': [{'time': '2022-01-01T00:00:00', 'location': 'USA'}]}

	result = analytics.get_url_stats('nonexistent')
	assert result == None


def test_record_click():
	analytics.url_data = {}
	analytics.record_click('test', 'USA')
	assert 'test' in analytics.url_data
	assert 'clicks' in analytics.url_data['test']
	assert isinstance(analytics.url_data['test']['clicks'][0]['time'], str)
	assert analytics.url_data['test']['clicks'][0]['location'] == 'USA'
