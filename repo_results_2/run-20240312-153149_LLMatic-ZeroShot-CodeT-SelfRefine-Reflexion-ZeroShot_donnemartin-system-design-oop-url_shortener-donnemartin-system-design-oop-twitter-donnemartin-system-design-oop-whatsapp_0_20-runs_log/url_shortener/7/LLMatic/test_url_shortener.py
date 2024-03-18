import url_shortener
import datetime

def test_generate_short_url():
	shortener = url_shortener.URLShortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert short_url is not None
	assert shortener.DATABASE[url]['short_url'] == short_url
	assert shortener.DATABASE[url]['expiration_date'] > datetime.datetime.now()

def test_custom_short_link():
	shortener = url_shortener.URLShortener()
	url = 'https://www.google.com'
	custom_link = 'custom'
	short_url = shortener.custom_short_link(url, custom_link)
	assert short_url == custom_link
	assert shortener.DATABASE[url]['short_url'] == custom_link
	assert shortener.DATABASE[url]['expiration_date'] > datetime.datetime.now()

def test_get_original_url():
	shortener = url_shortener.URLShortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert shortener.get_original_url(short_url) == url
	shortener.DATABASE[url]['expiration_date'] = datetime.datetime.now() - datetime.timedelta(days=1)
	assert shortener.get_original_url(short_url) is None

