import pytest
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views)

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'


def test_login_fail(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json()['message'] == 'Invalid credentials'


def test_reset_password(client):
	response = client.post('/reset-password', json={'email': 'test@test.com'})
	assert response.status_code == 200
	token = response.get_json()['token']
	response = client.post('/confirm-reset', json={'email': 'test@test.com', 'token': token, 'new_password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset successfully'
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'new_test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

