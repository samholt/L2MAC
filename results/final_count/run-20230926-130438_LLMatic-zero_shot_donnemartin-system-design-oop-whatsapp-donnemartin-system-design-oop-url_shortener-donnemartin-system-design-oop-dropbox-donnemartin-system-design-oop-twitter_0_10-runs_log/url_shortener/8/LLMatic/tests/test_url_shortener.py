import pytest
from services.url_shortener import UrlShortener
from datetime import datetime, timedelta


def test_url_shortener():
	url_shortener = UrlShortener()
	url = 'http://example.com'
	short_url = url_shortener.generate_short_url(url)
	assert url_shortener.get_original_url(short_url) == url
	assert url_shortener.get_original_url('invalid') is None

	# Test custom short URL
	custom_short_url = 'custom'
	assert url_shortener.generate_short_url(url, custom_short_url=custom_short_url) == custom_short_url
	assert url_shortener.generate_short_url(url, custom_short_url=custom_short_url) == 'Error: This custom short URL is not available'

	# Test analytics
	assert url_shortener.get_analytics(short_url) == {'clicks': 0, 'click_details': []}
	url_shortener.record_click(short_url, 'mocked_location')
	analytics = url_shortener.get_analytics(short_url)
	assert analytics['clicks'] == 1
	assert len(analytics['click_details']) == 1
	assert analytics['click_details'][0]['location'] == 'mocked_location'
	assert 'timestamp' in analytics['click_details'][0]

	# Test URL expiration
	expired_url = url_shortener.generate_short_url(url, datetime.now() - timedelta(days=1))
	assert url_shortener.get_original_url(expired_url) == 'Error: This URL has expired'
