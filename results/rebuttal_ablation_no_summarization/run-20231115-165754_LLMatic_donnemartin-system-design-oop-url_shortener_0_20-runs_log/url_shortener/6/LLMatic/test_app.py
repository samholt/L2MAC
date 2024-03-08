import pytest
from app import app, URL_DB, ANALYTICS_DB, USER_DB
from datetime import datetime, timedelta


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
		assert USER_DB['test'].id == 'test'
		resp = c.post('/register', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()

def test_login():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		resp = c.post('/login', json={'username': 'test', 'password': 'wrong'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()

def test_shorten_url():
	with app.test_client() as c:
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		assert resp.status_code == 401
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		assert resp.status_code == 200
		short_url = resp.get_json().get('short_url')
		assert short_url in URL_DB
		assert URL_DB[short_url]['url'] == 'https://www.google.com'
		assert URL_DB[short_url]['owner'] == 'test'
		resp = c.post('/shorten', json={'url': 'not a url', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_url': 'custom', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		assert resp.status_code == 200
		assert 'custom' in URL_DB
		assert URL_DB['custom']['url'] == 'https://www.google.com'
		assert URL_DB['custom']['owner'] == 'test'
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_url': 'custom', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()

def test_redirect_url():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.get('/' + short_url)
		assert resp.status_code == 302
		assert resp.headers['Location'] == 'https://www.google.com'
		resp = c.get('/invalid_url')
		assert resp.status_code == 404
		assert 'error' in resp.get_json()
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.get('/' + short_url)
		assert resp.status_code == 404
		assert 'error' in resp.get_json()

def test_edit_url():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.put('/' + short_url, json={'url': 'https://www.example.com'})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert URL_DB[short_url]['url'] == 'https://www.example.com'
		resp = c.put('/invalid_url', json={'url': 'https://www.example.com'})
		assert resp.status_code == 404
		assert 'error' in resp.get_json()
		resp = c.put('/' + short_url, json={'url': 'not a url'})
		assert resp.status_code == 400
		assert 'error' in resp.get_json()

def test_delete_url():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.delete('/' + short_url)
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert short_url not in URL_DB
		resp = c.delete('/invalid_url')
		assert resp.status_code == 404
		assert 'error' in resp.get_json()

def test_analytics():
	with app.test_client() as c:
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.get('/' + short_url)
		assert resp.status_code == 302
		assert ANALYTICS_DB[short_url]['access_time'] <= datetime.now()
		assert isinstance(ANALYTICS_DB[short_url]['location'], str)

def test_admin_dashboard():
	with app.test_client() as c:
		resp = c.post('/register', json={'username': 'admin', 'password': 'admin', 'is_admin': True})
		resp = c.post('/login', json={'username': 'admin', 'password': 'admin'})
		resp = c.get('/admin')
		assert resp.status_code == 200
		assert 'users' in resp.get_json()
		assert 'urls' in resp.get_json()
		resp = c.delete('/admin', json={'username': 'test'})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert 'test' not in USER_DB
		resp = c.post('/shorten', json={'url': 'https://www.google.com', 'expiration_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
		short_url = resp.get_json().get('short_url')
		resp = c.delete('/admin', json={'short_url': short_url})
		assert resp.status_code == 200
		assert 'message' in resp.get_json()
		assert short_url not in URL_DB
		resp = c.post('/register', json={'username': 'test', 'password': 'test'})
		resp = c.post('/login', json={'username': 'test', 'password': 'test'})
		resp = c.get('/admin')
		assert resp.status_code == 403
		assert 'error' in resp.get_json()

