import pytest
from unittest.mock import patch, MagicMock
from app import app, url_db, user_db
from datetime import datetime


def test_home():
	with app.test_client() as c:
		response = c.get('/')
		assert response.data == b'Hello, World!'


def test_register():
	with app.test_client() as c:
		response = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'test' in user_db

		# Test duplicate username
		response = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 400

		# Test without username or password
		response = c.post('/register', json={})
		assert response.status_code == 400

def test_login():
	with app.test_client() as c:
		# Test valid login
		response = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200

		# Test invalid login
		response = c.post('/login', json={'username': 'test', 'password': 'wrong'})
		assert response.status_code == 400

		# Test without username or password
		response = c.post('/login', json={})
		assert response.status_code == 400

def test_shorten_url():
	with app.test_client() as c:
		response = c.post('/shorten_url', json={'username': 'test', 'url': 'https://www.google.com', 'expiration_date': '2022-12-31T23:59:59'})
		assert response.status_code == 200
		shortened_url = response.get_json()['shortened_url']
		assert url_db[shortened_url]['url'] == 'https://www.google.com'
		assert shortened_url in user_db['test']['urls']
		assert url_db[shortened_url]['expiration_date'] == '2022-12-31T23:59:59'

		# Test custom alias
		response = c.post('/shorten_url', json={'username': 'test', 'url': 'https://www.google.com', 'alias': 'google', 'expiration_date': '2022-12-31T23:59:59'})
		assert response.status_code == 200
		assert url_db['google']['url'] == 'https://www.google.com'
		assert 'google' in user_db['test']['urls']
		assert url_db['google']['expiration_date'] == '2022-12-31T23:59:59'

		# Test duplicate alias
		response = c.post('/shorten_url', json={'username': 'test', 'url': 'https://www.google.com', 'alias': 'google', 'expiration_date': '2022-12-31T23:59:59'})
		assert response.status_code == 400

		# Test without username or url
		response = c.post('/shorten_url', json={})
		assert response.status_code == 400

def test_redirect_url():
	with app.test_client() as c:
		# Test valid shortened URL
		url_db['test'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '9999-12-31T23:59:59'}
		response = c.get('/test')
		assert response.status_code == 302
		assert response.location == 'https://www.google.com'
		assert len(url_db['test']['clicks']) == 1
		assert 'timestamp' in url_db['test']['clicks'][0]

		# Test expired shortened URL
		url_db['expired'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '2000-01-01T00:00:00'}
		response = c.get('/expired')
		assert response.status_code == 404

		# Test invalid shortened URL
		response = c.get('/invalid')
		assert response.status_code == 404

def test_analytics():
	with app.test_client() as c:
		# Test valid username
		url_db['test'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '9999-12-31T23:59:59'}
		url_db['google'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '9999-12-31T23:59:59'}
		user_db['test']['urls'] = ['test', 'google']
		response = c.get('/analytics/test')
		assert response.status_code == 200
		assert response.get_json() == {'test': url_db['test']['clicks'], 'google': url_db['google']['clicks']}

		# Test invalid username
		response = c.get('/analytics/invalid')
		assert response.status_code == 404

def test_delete_url():
	with app.test_client() as c:
		# Test valid username and shortened URL
		url_db['test'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '9999-12-31T23:59:59'}
		user_db['test']['urls'] = ['test']
		response = c.post('/delete_url', json={'username': 'test', 'short_url': 'test'})
		assert response.status_code == 200
		assert 'test' not in url_db
		assert 'test' not in user_db['test']['urls']

		# Test invalid username or shortened URL
		response = c.post('/delete_url', json={'username': 'test', 'short_url': 'invalid'})
		assert response.status_code == 400

		# Test without username or shortened URL
		response = c.post('/delete_url', json={})
		assert response.status_code == 400

def test_admin_urls():
	with app.test_client() as c:
		response = c.get('/admin/urls')
		assert response.status_code == 200
		assert response.get_json() == url_db

def test_admin_delete_url():
	with app.test_client() as c:
		# Test valid shortened URL
		url_db['test'] = {'url': 'https://www.google.com', 'clicks': [], 'username': 'test', 'expiration_date': '9999-12-31T23:59:59'}
		response = c.delete('/admin/url', json={'short_url': 'test'})
		assert response.status_code == 200
		assert 'test' not in url_db

		# Test invalid shortened URL
		response = c.delete('/admin/url', json={'short_url': 'invalid'})
		assert response.status_code == 400

		# Test without shortened URL
		response = c.delete('/admin/url', json={})
		assert response.status_code == 400

def test_admin_delete_user():
	with app.test_client() as c:
		# Test valid username
		user_db['test'] = {'password': 'test', 'urls': []}
		response = c.delete('/admin/user', json={'username': 'test'})
		assert response.status_code == 200
		assert 'test' not in user_db

		# Test invalid username
		response = c.delete('/admin/user', json={'username': 'invalid'})
		assert response.status_code == 400

		# Test without username
		response = c.delete('/admin/user', json={})
		assert response.status_code == 400

def test_admin_analytics():
	with app.test_client() as c:
		response = c.get('/admin/analytics')
		assert response.status_code == 200
		assert response.get_json() == {'user_count': len(user_db), 'url_count': len(url_db), 'click_count': sum(len(url_db[url]['clicks']) for url in url_db)}
