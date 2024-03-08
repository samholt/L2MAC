import pytest
from flask import Flask
from views import views
from models import users_db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.register_blueprint(views)

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'test@test.com' in users_db
	assert users_db['test@test.com'].username == 'test'
	assert users_db['test@test.com'].password != 'test'


def test_login(client):
	users_db['test@test.com'] = User('test@test.com', 'test', generate_password_hash('test'))
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()
