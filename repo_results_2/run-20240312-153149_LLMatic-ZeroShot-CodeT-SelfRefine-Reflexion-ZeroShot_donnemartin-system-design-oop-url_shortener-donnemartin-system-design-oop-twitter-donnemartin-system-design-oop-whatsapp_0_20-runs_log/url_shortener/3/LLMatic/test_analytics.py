import analytics
import datetime


def test_track_click():
	analytics.track_click('test_url', '8.8.8.8')
	clicks = analytics.get_statistics('test_url')
	assert len(clicks) == 1
	assert 'time' in clicks[0]
	assert isinstance(clicks[0]['time'], datetime.datetime)
	assert 'location' in clicks[0]


def test_get_statistics():
	clicks = analytics.get_statistics('test_url')
	assert len(clicks) == 1
	click = clicks[0]
	assert 'time' in click
	assert isinstance(click['time'], datetime.datetime)
	assert 'location' in click
