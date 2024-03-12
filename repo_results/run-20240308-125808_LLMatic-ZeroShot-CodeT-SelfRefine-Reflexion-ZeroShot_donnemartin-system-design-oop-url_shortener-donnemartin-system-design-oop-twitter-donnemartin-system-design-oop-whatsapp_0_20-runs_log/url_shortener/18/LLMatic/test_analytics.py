import analytics
import datetime

def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	click_data = analytics.get_click_data('test_url')
	assert len(click_data) == 1
	assert isinstance(click_data[0]['time'], datetime.datetime)
	assert click_data[0]['ip_address'] == '8.8.8.8'

def test_get_click_data():
	click_data = analytics.get_click_data('non_existent_url')
	assert click_data == []
