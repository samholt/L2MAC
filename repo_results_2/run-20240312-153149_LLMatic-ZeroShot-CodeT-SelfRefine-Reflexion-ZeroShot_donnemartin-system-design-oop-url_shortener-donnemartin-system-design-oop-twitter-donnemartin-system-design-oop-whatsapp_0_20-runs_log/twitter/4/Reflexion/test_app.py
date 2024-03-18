import pytest
import app
import json
from werkzeug.security import check_password_hash

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup():
	app.users = {}
	app.sessions = {}

@pytest.mark.usefixtures('setup')
def test_register(client):
	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Registered successfully' in response.get_data(as_text=True)
	assert 'test@test.com' in app.users
	assert check_password_hash(app.users['test@test.com']['password'], 'password')

@pytest.mark.usefixtures('setup')
def test_login(client):
	app.users['test@test.com'] = {'password': app.generate_password_hash('password', method='sha256')}
	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'token' in response.get_data(as_text=True)
	assert 'test@test.com' in app.sessions

@pytest.mark.usefixtures('setup')
def test_logout(client):
	app.sessions['test@test.com'] = 'token'
	response = client.post('/logout', data=json.dumps({'email': 'test@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Logged out successfully' in response.get_data(as_text=True)
	assert 'test@test.com' not in app.sessions
