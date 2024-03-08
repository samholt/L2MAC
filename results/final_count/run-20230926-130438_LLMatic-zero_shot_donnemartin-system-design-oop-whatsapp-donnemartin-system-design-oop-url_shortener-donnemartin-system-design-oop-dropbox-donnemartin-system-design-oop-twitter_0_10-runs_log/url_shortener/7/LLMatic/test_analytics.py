import analytics
from collections import defaultdict


def test_track_click():
	analytics.analytics_db = defaultdict(list)
	analytics.track_click('abc123', 'USA')
	assert len(analytics.analytics_db['abc123']) == 1


def test_get_statistics():
	analytics.analytics_db = defaultdict(list)
	analytics.track_click('abc123', 'USA')
	stats = analytics.get_statistics('abc123')
	assert stats['clicks'] == 1
	assert stats['details'][0]['location'] == 'USA'
