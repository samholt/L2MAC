import pytest
from datetime import datetime, timedelta
from url_shortener.models import User, URL, Click
from url_shortener.shortener import create_shortened_url
from main import app, DB


def test_redirect_to_original():
	user = User('test_user', 'password')
	original_url = 'http://example.com'
	shortened_url = create_shortened_url(original_url, user)
	DB['urls'].append(shortened_url)

	with app.test_client() as client:
		short_code = shortened_url.shortened_url.split('/')[-1]
		response = client.get(f'/{short_code}')
		assert response.status_code == 302
		assert response.location == original_url

		assert len(DB['clicks']) == 1
		click = DB['clicks'][0]
		assert click.url == shortened_url
		assert click.clicked_at.date() == datetime.now().date()
		assert click.location is not None


def test_redirect_to_expired():
	user = User('test_user', 'password')
	original_url = 'http://example.com'
	shortened_url = create_shortened_url(original_url, user, expires_in=timedelta(seconds=-1))
	DB['urls'].append(shortened_url)

	with app.test_client() as client:
		short_code = shortened_url.shortened_url.split('/')[-1]
		response = client.get(f'/{short_code}')
		assert response.status_code == 404
		assert response.data == b'URL has expired!'

