import analytics


def test_record_click():
	analytics.record_click('test_url')
	assert len(analytics.analytics_db['test_url']) == 1


def test_get_analytics():
	analytics.record_click('test_url')
	analytics_data = analytics.get_analytics('test_url')
	assert len(analytics_data) == 2
