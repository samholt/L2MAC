import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Clear mock database after each test
	app.urls_db.clear()
	app.users_db.clear()


def test_shorten_url(client):
	# Test URL shortening
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()

	# Test custom alias
	response = client.post('/shorten', json={'url': 'http://example.com', 'alias': 'custom'})
	assert response.status_code == 200
	assert response.get_json()['shortened_url'] == 'custom'

	# Test duplicate alias
	response = client.post('/shorten', json={'url': 'http://example.com', 'alias': 'custom'})
	assert response.status_code == 400


def test_redirect_url(client):
	# Test URL redirection
	client.post('/shorten', json={'url': 'http://example.com', 'alias': 'redirect'})
	response = client.get('/redirect')
	assert response.status_code == 302
	assert response.location == 'http://example.com'

	# Test non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404

	# Test expired URL
	client.post('/shorten', json={'url': 'http://example.com', 'alias': 'expired', 'expiration': (datetime.datetime.now() - datetime.timedelta(minutes=1)).isoformat()})
	response = client.get('/expired')
	assert response.status_code == 410


def test_get_analytics(client):
	# Test URL analytics
	client.post('/shorten', json={'url': 'http://example.com', 'alias': 'analytics'})
	client.get('/analytics')
	response = client.get('/analytics/analytics')
	assert response.status_code == 200
	assert response.get_json()['clicks'] == 1

	# Test non-existent URL
	response = client.get('/analytics/nonexistent')
	assert response.status_code == 404


def test_create_user(client):
	# Test user creation
	response = client.post('/user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 200

	# Test duplicate username
	response = client.post('/user', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 400


def test_get_user(client):
	# Test get user
	client.post('/user', json={'username': 'test', 'password': 'password'})
	response = client.get('/user/test')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'

	# Test non-existent user
	response = client.get('/user/nonexistent')
	assert response.status_code == 404
