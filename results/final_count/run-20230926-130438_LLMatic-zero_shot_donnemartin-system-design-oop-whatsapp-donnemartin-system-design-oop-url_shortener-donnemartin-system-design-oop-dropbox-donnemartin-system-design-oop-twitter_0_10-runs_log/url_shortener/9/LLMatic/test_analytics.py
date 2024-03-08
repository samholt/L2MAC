import pytest
from analytics import Analytics

def test_analytics():
	analytics = Analytics()
	short_url = 'abc123'
	assert analytics.retrieve(short_url) == 0
	analytics.record(short_url)
	assert analytics.retrieve(short_url) == 1
	analytics.record(short_url)
	assert analytics.retrieve(short_url) == 2
