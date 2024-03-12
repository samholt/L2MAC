import pytest
import app
from url_shortener import url_db
from user import User


def test_shorten_url():
	app.app.testing = True
	client = app.app.test_client()

	response = client.post('/shorten', json={'url': 'http://test.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_manage_user():
	app.app.testing = True
	client = app.app.test_client()

	# Test POST method
	response = client.post('/user', json={'username': 'testuser', 'password': 'testpassword'})
	assert response.status_code == 200
	assert response.get_json()['status'] == 'User created'
	assert 'user' in response.get_json()

	# Test PUT method
	response = client.put('/user', json={'username': 'testuser', 'new_username': 'newuser', 'new_password': 'newpassword'})
	assert response.status_code == 200
	assert response.get_json()['status'] == 'User updated'
	assert 'user' in response.get_json()

	# Test DELETE method
	response = client.delete('/user', json={'username': 'newuser'})
	assert response.status_code == 200
	assert response.get_json()['status'] == 'User deleted'


def test_admin_dashboard():
	app.app.testing = True
	client = app.app.test_client()

	# Test GET method
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'users' in response.get_json()
	assert 'urls' in response.get_json()

	# Test DELETE method
	test_user = User('testuser', 'testpassword')
	url_db['testurl'] = 'http://test.com'
	response = client.delete('/admin', json={'user': test_user.username, 'url': 'testurl'})
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'
	assert test_user not in User.users
	assert 'testurl' not in url_db


def test_admin_analytics():
	app.app.testing = True
	client = app.app.test_client()

	response = client.get('/admin/analytics/testurl')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
	assert 'click_info' in response.get_json()
