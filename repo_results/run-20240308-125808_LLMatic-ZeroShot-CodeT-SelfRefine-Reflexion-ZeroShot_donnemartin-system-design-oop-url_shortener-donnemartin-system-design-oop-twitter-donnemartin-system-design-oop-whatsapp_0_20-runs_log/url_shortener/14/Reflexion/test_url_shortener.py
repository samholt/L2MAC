import pytest
import url_shortener as us


def test_is_valid_url():
	assert us.is_valid_url('https://www.google.com')
	assert not us.is_valid_url('invalid_url')


def test_generate_short_url():
	url1 = us.generate_short_url()
	url2 = us.generate_short_url()
	assert len(url1) == 6
	assert len(url2) == 6
	assert url1 != url2


def test_shorten_url():
	response = us.shorten_url({'url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()

	response = us.shorten_url({'url': 'invalid_url'})
	assert response.status_code == 400
	assert 'error' in response.get_json()


def test_redirect_to_original():
	response = us.shorten_url({'url': 'https://www.google.com'})
	short_url = response.get_json()['shortened_url']

	response = us.redirect_to_original(short_url)
	assert response.status_code == 302

	response = us.redirect_to_original('invalid_short_url')
	assert response.status_code == 404
	assert 'error' in response.get_json()


def test_get_url_stats():
	response = us.shorten_url({'url': 'https://www.google.com'})
	short_url = response.get_json()['shortened_url']

	response = us.get_url_stats(short_url)
	assert response.status_code == 200
	assert 'original_url' in response.get_json()
	assert 'clicks' in response.get_json()

	response = us.get_url_stats('invalid_short_url')
	assert response.status_code == 404
	assert 'error' in response.get_json()
