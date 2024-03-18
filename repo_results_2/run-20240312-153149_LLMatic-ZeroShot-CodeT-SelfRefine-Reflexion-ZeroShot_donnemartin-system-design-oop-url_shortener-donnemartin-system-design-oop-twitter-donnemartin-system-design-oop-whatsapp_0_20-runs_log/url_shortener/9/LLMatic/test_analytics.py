import pytest
from analytics import Analytics


def test_track_and_retrieve_clicks():
	analytics = Analytics()
	short_url = 'abc123'
	location = 'USA'
	analytics.track_click(short_url, location)
	assert analytics.get_clicks(short_url) == 1
	click_details = analytics.get_click_details(short_url)
	assert len(click_details) == 1
	assert click_details[0]['location'] == location
