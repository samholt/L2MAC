import analytics
import datetime

def test_track_click():
	analytics.track_click('abc123', 'USA')
	click_data = analytics.get_click_data('abc123')
	assert len(click_data) == 1
	assert click_data[0]['location'] == 'USA'


def test_get_click_data():
	click_data = analytics.get_click_data('abc123')
	assert len(click_data) == 1
	assert click_data[0]['location'] == 'USA'
	assert isinstance(click_data[0]['time'], datetime.datetime)
