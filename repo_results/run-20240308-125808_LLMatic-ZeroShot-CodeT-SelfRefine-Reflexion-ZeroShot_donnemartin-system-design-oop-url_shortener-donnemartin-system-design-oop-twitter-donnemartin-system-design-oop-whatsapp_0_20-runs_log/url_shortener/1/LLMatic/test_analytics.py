import analytics
import datetime


def test_record_click():
	an = analytics.Analytics()
	an.record_click('abc123', 'USA')
	assert len(an.get_statistics('abc123')) == 1
	assert an.get_statistics('abc123')[0]['location'] == 'USA'


def test_get_statistics():
	an = analytics.Analytics()
	an.record_click('abc123', 'USA')
	an.record_click('abc123', 'Canada')
	assert len(an.get_statistics('abc123')) == 2
	assert an.get_statistics('abc123')[0]['location'] == 'USA'
	assert an.get_statistics('abc123')[1]['location'] == 'Canada'
