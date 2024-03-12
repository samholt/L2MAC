import analytics
import datetime

def test_track_click():
	analytics.track_click('test_url', '128.101.101.101')
	click_data = analytics.get_click_data('test_url')
	assert len(click_data) == 1
	assert 'time' in click_data[0]
	assert 'ip_address' in click_data[0]
	assert isinstance(click_data[0]['time'], datetime.datetime)

def test_get_click_data():
	click_data = analytics.get_click_data('non_existent_url')
	assert click_data == []
