import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	with app.app_context():
		db.create_all()
		yield
		db.drop_all()

def test_register(client, init_database):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'msg': 'User created successfully'}

def test_login(client, init_database):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()
