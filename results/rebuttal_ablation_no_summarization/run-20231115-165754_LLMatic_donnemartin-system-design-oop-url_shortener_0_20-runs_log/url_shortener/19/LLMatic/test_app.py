import pytest
from app import app


def test_shorten_url():
	with app.test_client() as c:
		response = c.post('/shorten_url', data={'url': 'https://www.google.com', 'expiration_minutes': 10})
		assert response.status_code == 200
		short_url = response.data.decode()
		assert len(short_url) == 10


def test_redirect_url():
	with app.test_client() as c:
		response = c.post('/shorten_url', data={'url': 'https://www.google.com', 'expiration_minutes': 10})
		short_url = response.data.decode()
		response = c.get('/' + short_url)
		assert response.status_code == 302
		assert response.location == 'https://www.google.com'


def test_analytics():
	with app.test_client() as c:
		response = c.post('/shorten_url', data={'url': 'https://www.google.com', 'expiration_minutes': 10})
		short_url = response.data.decode()
		c.get('/' + short_url)
		response = c.get('/analytics/' + short_url)
		assert response.status_code == 200
		assert len(response.data.decode()) > 0


def test_user_accounts():
	with app.test_client() as c:
		response = c.post('/create_account', data={'username': 'testuser'})
		assert response.status_code == 200
		assert response.data.decode() == 'Account created successfully.'
		response = c.get('/view_urls/testuser')
		assert response.status_code == 200
		assert response.data.decode() == '{}'
		response = c.post('/edit_url', data={'username': 'testuser', 'old_url': 'https://www.google.com', 'new_url': 'https://www.bing.com'})
		assert response.status_code == 200
		assert response.data.decode() == 'URL does not exist.'
		response = c.post('/delete_url', data={'username': 'testuser', 'url': 'https://www.google.com'})
		assert response.status_code == 200
		assert response.data.decode() == 'URL does not exist.'
		response = c.post('/delete_user', data={'username': 'testuser'})
		assert response.status_code == 200
		assert response.data.decode() == 'User deleted successfully.'
