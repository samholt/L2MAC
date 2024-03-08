import pytest
from app import app


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'

def test_register():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert resp.get_json()['message'] == 'User registered successfully'

		resp = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Username already exists'

def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert resp.get_json()['message'] == 'Logged in successfully'

		resp = c.post('/login', json={'username': 'test', 'password': 'wrong'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Invalid username or password'

def test_logout():
	with app.test_client() as c:
		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.get('/logout')
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert resp.get_json()['message'] == 'Logged out successfully'

def test_shorten_url():
	with app.test_client() as c:
		resp = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		assert resp.status_code == 401
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Please log in'

		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		assert resp.status_code == 200
		assert 'short_url' in resp.get_json()
		assert resp.get_json()['short_url'] == 'http://short.url/test'

		resp = c.post('/shorten_url', json={'url': 'not a url'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Invalid URL'

def test_redirect_url():
	with app.test_client() as c:
		# Test redirection for an existing shortened URL
		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = resp.get_json()['short_url'].replace('http://short.url/', '')
		resp = c.get('/'+short_url)
		assert resp.status_code == 302
		assert resp.headers['Location'] == 'https://www.google.com'

		# Test redirection for a non-existent shortened URL
		resp = c.get('/nonexistenturl')
		assert resp.status_code == 404
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'URL not found'

def test_get_analytics():
	with app.test_client() as c:
		# Test analytics for an existing shortened URL
		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = resp.get_json()['short_url'].replace('http://short.url/', '')
		resp = c.get('/'+short_url)
		resp = c.get('/'+short_url)
		resp = c.get('/'+short_url)
		resp = c.get('/'+short_url)
		resp = c.get('/'+short_url)
		resp = c.get('/'+short_url)
		resp = c.get('/analytics/'+short_url)
		assert resp.status_code == 200
		assert 'analytics' in resp.get_json()
		assert len(resp.get_json()['analytics']) == 6

		# Test analytics for a non-existent shortened URL
		resp = c.get('/analytics/nonexistenturl')
		assert resp.status_code == 404
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'URL not found'

def test_get_user_urls():
	with app.test_client() as c:
		# Test getting URLs for a logged-in user
		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.get('/user/urls')
		assert resp.status_code == 200
		assert 'urls' in resp.get_json()
		assert len(resp.get_json()['urls']) == 1

		# Test getting URLs for a not logged-in user
		c.get('/logout')
		resp = c.get('/user/urls')
		assert resp.status_code == 401
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Please log in'

def test_get_user_analytics():
	with app.test_client() as c:
		# Test getting analytics for a logged-in user
		c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.get('/user/analytics')
		assert resp.status_code == 200
		assert 'analytics' in resp.get_json()
		assert len(resp.get_json()['analytics']) == 1

		# Test getting analytics for a not logged-in user
		c.get('/logout')
		resp = c.get('/user/analytics')
		assert resp.status_code == 401
		assert 'error' in resp.get_json()
		assert resp.get_json()['error'] == 'Please log in'


