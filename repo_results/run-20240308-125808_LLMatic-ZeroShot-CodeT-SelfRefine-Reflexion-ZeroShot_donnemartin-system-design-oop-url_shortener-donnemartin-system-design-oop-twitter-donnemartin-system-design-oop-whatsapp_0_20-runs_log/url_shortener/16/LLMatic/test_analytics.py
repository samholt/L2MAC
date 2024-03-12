import pytest
import analytics


def test_get_url_stats_no_url():
	assert analytics.get_url_stats('non_existent_url') == {'clicks': 0, 'click_info': []}


def test_get_url_stats_with_url():
	analytics.url_data['testurl'] = {'clicks': [{'time': '2022-01-01 00:00:00', 'location': 'USA'}]}
	assert analytics.get_url_stats('testurl') == {'clicks': 1, 'click_info': [{'time': '2022-01-01 00:00:00', 'location': 'USA'}]}


def test_record_click():
	analytics.record_click('testurl', 'USA')
	assert analytics.url_data['testurl']['clicks'][0]['location'] == 'USA'
