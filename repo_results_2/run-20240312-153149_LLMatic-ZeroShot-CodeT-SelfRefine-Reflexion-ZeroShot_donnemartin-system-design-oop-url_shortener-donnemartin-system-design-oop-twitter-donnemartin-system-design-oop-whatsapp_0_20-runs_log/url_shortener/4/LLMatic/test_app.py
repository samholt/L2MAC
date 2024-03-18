import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_account(client):
	# Test account creation
	response = client.post('/account', json={'username': 'test1', 'password': 'test1'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Account created'}

	# Test retrieving user URLs
	response = client.get('/account', json={'username': 'test1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {}

	# Test updating user URL
	response = client.put('/account', json={'username': 'test1', 'old_short_url': '1', 'new_short_url': '2'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL not found'}

	# Test deleting user URL
	response = client.delete('/account', json={'username': 'test1', 'short_url': '1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL not found'}


def test_analytics(client):
	# Test account creation
	response = client.post('/account', json={'username': 'test2', 'password': 'test2'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Account created'}

	# Test URL shortening
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_link': 'google2', 'username': 'test2'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)

	# Test retrieving user analytics
	response = client.get('/analytics/test2')
	assert response.status_code == 200
	assert 'google2' in json.loads(response.data)


def test_admin(client):
	# Test account creation
	response = client.post('/account', json={'username': 'test3', 'password': 'test3'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Account created'}

	# Test URL shortening
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'custom_short_link': 'google3', 'username': 'test3'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)

	# Test retrieving admin dashboard
	response = client.get('/admin')
	assert response.status_code == 200
	assert 'test3' in json.loads(response.data)

	# Test deleting user URL
	response = client.delete('/admin', json={'username': 'test3', 'short_url': 'google3'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL deleted'}

	# Test deleting user account
	response = client.delete('/admin', json={'username': 'test3'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Account deleted'}

