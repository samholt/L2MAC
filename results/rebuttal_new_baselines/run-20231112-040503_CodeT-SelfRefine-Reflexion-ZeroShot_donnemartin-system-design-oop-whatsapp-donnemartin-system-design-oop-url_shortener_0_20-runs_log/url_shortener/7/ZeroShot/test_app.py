import pytest
import app
import datetime

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	app.DB = {}


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()


def test_redirect_to_url(client):
	app.DB['test'] = app.URL(original='https://www.google.com', shortened='test', clicks=0, created_at=datetime.datetime.now(), expires_at=None, owner=None)
	response = client.get('/test')
	assert response.status_code == 302


def test_get_analytics(client):
	app.DB['test'] = app.URL(original='https://www.google.com', shortened='test', clicks=0, created_at=datetime.datetime.now(), expires_at=None, owner=None)
	response = client.get('/analytics', json={'alias': 'test'})
	assert response.status_code == 200
	assert 'original_url' in response.get_json()
	assert 'clicks' in response.get_json()
	assert 'created_at' in response.get_json()
	assert 'expires_at' in response.get_json()
