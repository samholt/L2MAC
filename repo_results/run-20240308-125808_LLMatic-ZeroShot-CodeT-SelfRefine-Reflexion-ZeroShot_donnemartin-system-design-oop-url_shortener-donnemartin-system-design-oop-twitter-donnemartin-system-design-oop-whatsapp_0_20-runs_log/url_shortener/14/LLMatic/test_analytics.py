import pytest
from analytics import Analytics


def test_analytics():
	analytics = Analytics()
	analytics.track('abc123', '2022-01-01T00:00:00', 'USA')
	analytics.track('abc123', '2022-01-02T00:00:00', 'USA')
	analytics.track('xyz789', '2022-01-03T00:00:00', 'Canada')

	assert analytics.retrieve('abc123') == [
		{'timestamp': '2022-01-01T00:00:00', 'location': 'USA'},
		{'timestamp': '2022-01-02T00:00:00', 'location': 'USA'}
	]
	assert analytics.retrieve('xyz789') == [
		{'timestamp': '2022-01-03T00:00:00', 'location': 'Canada'}
	]
	assert analytics.retrieve('nonexistent') == []
