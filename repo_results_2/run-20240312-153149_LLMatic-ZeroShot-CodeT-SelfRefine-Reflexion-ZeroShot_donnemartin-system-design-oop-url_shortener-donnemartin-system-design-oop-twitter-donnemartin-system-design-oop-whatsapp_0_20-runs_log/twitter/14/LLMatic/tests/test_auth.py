import pytest
import jwt
from flask import Flask, json
from views import views
from models import users_db, User

app = Flask(__name__)
app.register_blueprint(views)

@pytest.fixture

def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}
	assert isinstance(users_db['test'], User)


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'token' in data
	assert jwt.decode(data['token'], 'secret', algorithms=['HS256']) == {'username': 'test'}


def test_login_invalid_credentials(client):
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid credentials'}
