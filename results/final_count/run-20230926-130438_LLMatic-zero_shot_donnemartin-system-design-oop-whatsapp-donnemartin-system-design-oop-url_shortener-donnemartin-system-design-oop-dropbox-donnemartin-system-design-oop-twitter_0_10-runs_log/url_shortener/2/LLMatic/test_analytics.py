import analytics
import datetime


def test_track_click():
	"""Test that click events are tracked correctly."""
	analytics.track_click('abc123', '8.8.8.8')
	data = analytics.get_analytics('abc123')

	assert len(data) == 1
	assert isinstance(data[0]['time'], datetime.datetime)
	assert data[0]['ip_address'] == '8.8.8.8'


def test_get_analytics():
	"""Test that analytics data is retrieved correctly."""
	data = analytics.get_analytics('abc123')

	assert len(data) == 1
	assert isinstance(data[0]['time'], datetime.datetime)
	assert data[0]['ip_address'] == '8.8.8.8'
