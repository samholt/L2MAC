import pytest
from app import app, User, users, urls
from flask_login import login_user

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def user():
	user = User(id='test')
	users[user.id] = user
	return user

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'test' in users

def test_login(client, user):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

def test_shorten(client, user):
	login_user(user)
	response = client.post('/shorten', json={'original_url': 'https://example.com'})
	assert response.status_code == 201
	short_url = response.get_json()['short_url']
	assert short_url in urls

def test_redirect_to_original(client, user):
	login_user(user)
	response = client.post('/shorten', json={'original_url': 'https://example.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://example.com'

def test_analytics(client, user):
	login_user(user)
	response = client.post('/shorten', json={'original_url': 'https://example.com'})
	short_url = response.get_json()['short_url']
	client.get(f'/{short_url}')
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	data = response.get_json()
	assert data['clicks'] == 1
