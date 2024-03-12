import analytics
import datetime


def test_track_click():
	"""Test that clicks are tracked correctly."""
	short_url = 'abc123'
	ip_address = '8.8.8.8'

	# Track a click
	analytics.track_click(short_url, ip_address)

	# Check that the click was tracked
	click_data = analytics.get_analytics(short_url)
	assert len(click_data) == 1
	assert 'time' in click_data[0]
	assert 'ip_address' in click_data[0]
	assert isinstance(click_data[0]['time'], datetime.datetime)


def test_get_analytics():
	"""Test that analytics data is retrieved correctly."""
	short_url = 'abc123'

	# Check that the analytics data is correct
	click_data = analytics.get_analytics(short_url)
	assert len(click_data) == 1
	assert 'time' in click_data[0]
	assert 'ip_address' in click_data[0]
	assert isinstance(click_data[0]['time'], datetime.datetime)
