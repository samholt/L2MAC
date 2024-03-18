import pytest
from app import app
from datetime import datetime, timedelta
from models import URL
from shortener import Shortener


def test_expired_url():
	with app.test_client() as c:
		response = c.post('/register', data={'username': 'test', 'password': 'test', 'isAdmin': 'False'})
		assert response.status_code == 201
		response = c.post('/login', data={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		expired_url = URL('http://expired.com', 'expired', 'test', datetime.now() - timedelta(days=1))
		app.shortener = Shortener()
		app.shortener.urls['expired'] = expired_url
		response = c.get('/expired')
		assert response.status_code == 410
		assert response.data == b'URL has expired'


def test_not_expired_url():
	with app.test_client() as c:
		response = c.post('/register', data={'username': 'test1', 'password': 'test', 'isAdmin': 'False'})
		assert response.status_code == 201
		response = c.post('/login', data={'username': 'test1', 'password': 'test'})
		assert response.status_code == 200
		not_expired_url = URL('http://notexpired.com', 'notexpired', 'test1', datetime.now() + timedelta(days=1))
		app.shortener = Shortener()
		app.shortener.urls['notexpired'] = not_expired_url
		response = c.get('/notexpired')
		assert response.status_code == 302
		assert response.location == 'http://notexpired.com'

