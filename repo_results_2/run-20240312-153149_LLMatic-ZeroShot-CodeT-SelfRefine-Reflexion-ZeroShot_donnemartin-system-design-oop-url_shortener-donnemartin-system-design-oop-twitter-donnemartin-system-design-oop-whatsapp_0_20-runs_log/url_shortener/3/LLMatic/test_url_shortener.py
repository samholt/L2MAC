import url_shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url.isalnum()

	# Ensure uniqueness
	url2 = 'https://www.different.com'
	short_url2 = url_shortener.generate_short_url(url2)
	assert short_url != short_url2

	# Test custom short URL
	custom_short_url = 'custom'
	short_url3 = url_shortener.generate_short_url(url, custom_short_url)
	assert short_url3 == custom_short_url

	# Test custom short URL already in use
	short_url4 = url_shortener.generate_short_url(url, custom_short_url)
	assert short_url4 != custom_short_url

	# Test expiration date
	expiration_date = (datetime.now() + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
	short_url5 = url_shortener.generate_short_url(url, expiration_date=expiration_date)
	assert not url_shortener.is_expired(short_url5)


def test_validate_url():
	assert url_shortener.validate_url('https://www.example.com')
	assert not url_shortener.validate_url('https://www.invalidurl.com')


def test_is_expired():
	# Test non-expired URL
	expiration_date = (datetime.now() + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
	short_url = url_shortener.generate_short_url('https://www.example.com', expiration_date=expiration_date)
	assert not url_shortener.is_expired(short_url)

	# Test expired URL
	expiration_date = (datetime.now() - timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
	short_url = url_shortener.generate_short_url('https://www.example.com', expiration_date=expiration_date)
	assert url_shortener.is_expired(short_url)
