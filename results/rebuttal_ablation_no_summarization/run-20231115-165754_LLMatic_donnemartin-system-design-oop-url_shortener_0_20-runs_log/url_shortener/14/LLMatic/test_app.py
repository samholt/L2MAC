import pytest
from app import app, DATABASE
from datetime import datetime, timedelta
import time

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 302
	assert 'test' in DATABASE['users']


def test_login(client):
	client.post('/register', data={'username': 'test', 'password': 'test'})
	response = client.post('/login', data={'username': 'test', 'password': 'test'})
	assert response.status_code == 302


def test_submit_url(client):
	client.post('/register', data={'username': 'test', 'password': 'test'})
	response = client.post('/submit', data={'url': 'http://example.com', 'username': 'test'})
	assert response.status_code == 302
	assert 'http://example.com' in DATABASE['urls']['test'].values()


def test_redirect_to_url(client):
	client.post('/register', data={'username': 'test', 'password': 'test'})
	client.post('/submit', data={'url': 'http://example.com', 'username': 'test'})
	short_url = list(DATABASE['urls']['test'].keys())[0]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_expiration(client):
	client.post('/register', data={'username': 'test', 'password': 'test'})
	expiration_date = (datetime.now() + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
	client.post('/submit', data={'url': 'http://example.com', 'username': 'test', 'expiration_date': expiration_date})
	short_url = list(DATABASE['urls']['test'].keys())[0]
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	time.sleep(6)
	response = client.get(f'/{short_url}')
	assert response.status_code == 410
	assert short_url not in DATABASE['urls']['test']
