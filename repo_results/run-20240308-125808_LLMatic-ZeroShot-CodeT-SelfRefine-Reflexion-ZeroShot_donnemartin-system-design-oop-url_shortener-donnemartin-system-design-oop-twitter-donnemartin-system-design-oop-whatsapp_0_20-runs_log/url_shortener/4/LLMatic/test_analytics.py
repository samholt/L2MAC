import analytics
import datetime


def test_record_click():
	analytics.analytics_db.clear()
	analytics.record_click('test_url', '128.101.101.101')
	assert len(analytics.analytics_db['test_url']) == 1


def test_get_click_count():
	analytics.analytics_db.clear()
	analytics.record_click('test_url', '128.101.101.101')
	assert analytics.get_click_count('test_url') == 1


def test_get_click_details():
	analytics.analytics_db.clear()
	analytics.record_click('test_url', '128.101.101.101')
	click_details = analytics.get_click_details('test_url')
	assert len(click_details) == 1
	assert isinstance(click_details[0][0], datetime.datetime)
	assert isinstance(click_details[0][1], str)
