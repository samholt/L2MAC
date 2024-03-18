import json
import views
from models import URL, Click, User
from datetime import datetime, timedelta


def test_shorten_url():
	with views.app.test_client() as c:
		response = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		data = json.loads(response.data)
		assert 'shortened_url' in data
		assert len(data['shortened_url']) == 6


def test_redirect_to_original():
	with views.app.test_client() as c:
		response = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		data = json.loads(response.data)
		response = c.get('/' + data['shortened_url'])
		assert response.status_code == 302


def test_get_stats():
	with views.app.test_client() as c:
		response = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		data = json.loads(response.data)
		response = c.get('/stats/' + data['shortened_url'])
		data = json.loads(response.data)
		assert 'clicks' in data


def test_create_user_route():
	with views.app.test_client() as c:
		response = c.post('/create_user', json={'username': 'test', 'password': 'password'})
		data = json.loads(response.data)
		assert 'user' in data
		assert data['user']['username'] == 'test'
		assert data['user']['password'] == 'password'


def test_get_user_route():
	with views.app.test_client() as c:
		c.post('/create_user', json={'username': 'test', 'password': 'password'})
		response = c.get('/user/test')
		data = json.loads(response.data)
		assert 'user' in data
		assert data['user']['username'] == 'test'
		assert data['user']['password'] == 'password'


def test_edit_user_route():
	with views.app.test_client() as c:
		c.post('/create_user', json={'username': 'test', 'password': 'password'})
		response = c.put('/user/test', json={'new_password': 'new_password'})
		data = json.loads(response.data)
		assert 'user' in data
		assert data['user']['username'] == 'test'
		assert data['user']['password'] == 'new_password'


def test_delete_user_route():
	with views.app.test_client() as c:
		c.post('/create_user', json={'username': 'test', 'password': 'password'})
		response = c.delete('/user/test')
		data = json.loads(response.data)
		assert 'message' in data
		assert data['message'] == 'User deleted'


def test_get_all_urls_route():
	with views.app.test_client() as c:
		c.post('/shorten_url', json={'url': 'https://www.google.com'})
		c.post('/shorten_url', json={'url': 'https://www.facebook.com'})
		response = c.get('/admin/urls')
		data = json.loads(response.data)
		assert 'urls' in data
		assert len(data['urls']) == 2


def test_delete_url_route():
	with views.app.test_client() as c:
		response = c.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = json.loads(response.data)['shortened_url']
		response = c.delete('/admin/url/' + short_url)
		data = json.loads(response.data)
		assert 'message' in data
		assert data['message'] == 'URL deleted'


def test_get_all_users_route():
	with views.app.test_client() as c:
		c.post('/create_user', json={'username': 'test1', 'password': 'password1'})
		c.post('/create_user', json={'username': 'test2', 'password': 'password2'})
		response = c.get('/admin/users')
		data = json.loads(response.data)
		assert 'users' in data
		assert len(data['users']) == 2
