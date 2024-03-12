import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_home(client):
	response = client.get('/')
	assert b'Welcome to the Chat Service' in response.data

def test_register(client):
	response = client.get('/register')
	assert b'Register' in response.data

def test_login(client):
	response = client.get('/login')
	assert b'Login' in response.data

def test_chat(client):
	response = client.get('/chat')
	assert b'Chat Interface' in response.data

def test_status(client):
	response = client.get('/status')
	assert b'Status/Story Feature' in response.data
