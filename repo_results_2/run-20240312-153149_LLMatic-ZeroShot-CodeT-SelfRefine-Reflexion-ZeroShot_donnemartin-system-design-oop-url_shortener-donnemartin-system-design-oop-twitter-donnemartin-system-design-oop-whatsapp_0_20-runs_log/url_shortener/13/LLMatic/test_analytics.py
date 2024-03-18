import pytest
import analytics


def test_track_click():
	analytics.track_click('test')
	assert 'test' in analytics.analytics_db


def test_get_statistics():
	stats = analytics.get_statistics('test')
	assert stats is not None


def test_get_system_performance():
	performance = analytics.get_system_performance()
	assert 'total_urls' in performance
	assert 'total_clicks' in performance
