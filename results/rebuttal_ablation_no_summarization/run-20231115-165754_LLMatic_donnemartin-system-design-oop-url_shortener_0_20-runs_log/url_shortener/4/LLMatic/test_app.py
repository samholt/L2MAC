import pytest
from app import app, url_db, user_db
from datetime import datetime, timedelta
import pytz


def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Hello, World!'


def test_create_account():
	with app.test_client() as c:
		# Test successful account creation
		resp = c.post('/create_account', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert user_db['test']['password'] == 'test'
		assert user_db['test']['urls'] == []

		# Test duplicate username
		resp = c.post('/create_account', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 400


def test_manage_url():
	with app.test_client() as c:
		# Test invalid username or password
		resp = c.post('/manage_url', json={'username': 'invalid', 'password': 'invalid', 'action': 'delete', 'short_link': 'invalid'})
		assert resp.status_code == 401

		# Test invalid short link
		resp = c.post('/manage_url', json={'username': 'test', 'password': 'test', 'action': 'delete', 'short_link': 'invalid'})
		assert resp.status_code == 404

		# Test successful URL deletion
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.post('/manage_url', json={'username': 'test', 'password': 'test', 'action': 'delete', 'short_link': short_link})
		assert resp.status_code == 200
		assert short_link not in url_db
		assert short_link not in user_db['test']['urls']

		# Test successful URL editing
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.post('/manage_url', json={'username': 'test', 'password': 'test', 'action': 'edit', 'short_link': short_link, 'new_url': 'https://google.com'})
		assert resp.status_code == 200
		assert url_db[short_link]['url'] == 'https://google.com'


def test_view_analytics():
	with app.test_client() as c:
		# Test invalid username or password
		resp = c.post('/view_analytics', json={'username': 'invalid', 'password': 'invalid'})
		assert resp.status_code == 401

		# Test successful analytics retrieval
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.get('/' + short_link)
		resp = c.post('/view_analytics', json={'username': 'test', 'password': 'test'})
		assert resp.status_code == 200
		assert len(resp.get_json()[short_link]) == 1
		assert 'timestamp' in resp.get_json()[short_link][0]
		assert 'location' in resp.get_json()[short_link][0]


def test_shorten_url():
	with app.test_client() as c:
		# Test invalid username or password
		resp = c.post('/shorten_url', json={'username': 'invalid', 'password': 'invalid', 'url': 'https://example.com'})
		assert resp.status_code == 401

		# Test successful URL shortening
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		assert resp.status_code == 200
		short_link = resp.get_json()['short_link']
		assert url_db[short_link]['url'] == 'https://example.com'
		assert url_db[short_link]['clicks'] == []
		assert short_link in user_db['test']['urls']

		# Test duplicate custom short link
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com', 'custom_short_link': short_link})
		assert resp.status_code == 400

		# Test successful URL shortening with expiration
		expiration = (datetime.now(pytz.utc) + timedelta(minutes=1)).isoformat()
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com', 'expiration': expiration})
		assert resp.status_code == 200
		short_link = resp.get_json()['short_link']
		assert url_db[short_link]['url'] == 'https://example.com'
		assert url_db[short_link]['clicks'] == []
		assert url_db[short_link]['expiration'] == expiration
		assert short_link in user_db['test']['urls']


def test_redirect_url():
	with app.test_client() as c:
		# Test invalid short link
		resp = c.get('/invalid_link')
		assert resp.status_code == 404

		# Test successful redirection and click recording
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.get('/' + short_link)
		assert resp.status_code == 302
		assert resp.headers['Location'] == 'https://example.com'
		assert len(url_db[short_link]['clicks']) == 1
		assert 'timestamp' in url_db[short_link]['clicks'][0]
		assert 'location' in url_db[short_link]['clicks'][0]

		# Test expired URL
		expiration = (datetime.now(pytz.utc) - timedelta(minutes=1)).isoformat()
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com', 'expiration': expiration})
		short_link = resp.get_json()['short_link']
		resp = c.get('/' + short_link)
		assert resp.status_code == 404


def test_get_stats():
	with app.test_client() as c:
		# Test invalid short link
		resp = c.get('/stats/invalid_link')
		assert resp.status_code == 404

		# Test successful statistics retrieval
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.get('/' + short_link)
		resp = c.get('/stats/' + short_link)
		assert resp.status_code == 200
		assert len(resp.get_json()) == 1
		assert 'timestamp' in resp.get_json()[0]
		assert 'location' in resp.get_json()[0]

# Admin dashboard tests

def test_admin_view_urls():
	with app.test_client() as c:
		# Test successful URL viewing
		resp = c.get('/admin/urls')
		assert resp.status_code == 200
		assert set(resp.get_json()) == set(url_db.keys())


def test_admin_delete_url():
	with app.test_client() as c:
		# Test invalid short link
		resp = c.delete('/admin/url/invalid_link')
		assert resp.status_code == 404

		# Test successful URL deletion
		resp = c.post('/shorten_url', json={'username': 'test', 'password': 'test', 'url': 'https://example.com'})
		short_link = resp.get_json()['short_link']
		resp = c.delete('/admin/url/' + short_link)
		assert resp.status_code == 200
		assert short_link not in url_db
		assert short_link not in user_db['test']['urls']


def test_admin_delete_user():
	with app.test_client() as c:
		# Test invalid username
		resp = c.delete('/admin/user/invalid_username')
		assert resp.status_code == 404

		# Test successful user deletion
		resp = c.delete('/admin/user/test')
		assert resp.status_code == 200
		assert 'test' not in user_db


def test_admin_view_analytics():
	with app.test_client() as c:
		# Test successful analytics retrieval
		resp = c.get('/admin/analytics')
		assert resp.status_code == 200
		assert resp.get_json()['total_users'] == len(user_db)
		assert resp.get_json()['total_urls'] == len(url_db)
		assert resp.get_json()['total_clicks'] == sum(len(url['clicks']) for url in url_db.values())

