import pytest
import app
from models import URL, User
from datetime import datetime, timedelta


def test_expired_url():
	app.app.shortener.urls = {}
	expired_url = URL('http://expired.com', 'expired', 'test', 0, [], datetime.now() - timedelta(days=1))
	app.app.shortener.urls['expired'] = expired_url
	with app.app.test_client() as c:
		response = c.get('/expired')
		assert response.status_code == 410
		assert b'URL has expired' in response.data


def test_not_expired_url():
	app.app.shortener.urls = {}
	not_expired_url = URL('http://notexpired.com', 'notexpired', 'test', 0, [], datetime.now() + timedelta(days=1))
	app.app.shortener.urls['notexpired'] = not_expired_url
	with app.app.test_client() as c:
		response = c.get('/notexpired')
		assert response.status_code == 302
		assert response.headers['Location'] == 'http://notexpired.com'
