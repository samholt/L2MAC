import pytest
from datetime import datetime, timedelta
from models import URL, URLShortener


def test_url():
	url = URL('https://example.com', 'ABCDE', datetime.now(), datetime.now() + timedelta(days=1))
	assert url.original_url == 'https://example.com'
	assert url.shortened_url == 'ABCDE'
	assert url.clicks == 0


def test_url_shortener():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://example.com', datetime.now() - timedelta(days=1))
	assert len(short_url) == 5
	assert url_shortener.get_original_url(short_url) == 'https://example.com'
	url_shortener.track_click(short_url)
	assert url_shortener.urls[short_url].clicks == 1
	url_shortener.delete_expired_urls()
	assert short_url not in url_shortener.urls
