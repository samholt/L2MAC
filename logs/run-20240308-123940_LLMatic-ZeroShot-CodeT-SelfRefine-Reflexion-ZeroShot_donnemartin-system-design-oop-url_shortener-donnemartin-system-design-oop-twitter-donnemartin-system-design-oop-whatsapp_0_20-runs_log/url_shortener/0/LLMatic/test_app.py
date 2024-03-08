import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 201


def test_redirect_to_url(client):
	response = client.get('/abcdef')
	assert response.status_code == 404


def test_view_analytics(client):
	response = client.get('/analytics/abcdef')
	assert response.status_code == 200


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
