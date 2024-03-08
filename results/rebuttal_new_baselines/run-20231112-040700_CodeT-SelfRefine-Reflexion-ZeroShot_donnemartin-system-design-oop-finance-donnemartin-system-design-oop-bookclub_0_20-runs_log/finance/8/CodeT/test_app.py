import pytest
import app
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def init_db():
	app.users_db = {}
	app.transactions_db = {}

@pytest.mark.usefixtures('init_db')
def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'test' in app.users_db
	assert app.users_db['test'].password == hashlib.sha256('test'.encode()).hexdigest()

@pytest.mark.usefixtures('init_db')
def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

@pytest.mark.usefixtures('init_db')
def test_login_invalid_credentials(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}
