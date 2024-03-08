import pytest
import json
from app import app, users_db
from app.models import User

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def init_database():
	user = User(
		id=1,
		name='Test User',
		email='test@example.com',
		password='testpassword',
		profile_picture='',
		storage_used=0
	)
	users_db[user.id] = user

	yield users_db

	users_db.clear()

def test_login_success(client, init_database):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'testpassword'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'

def test_login_incorrect_password(client, init_database):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'wrongpassword'}), content_type='application/json')
	assert response.status_code == 401
	assert response.get_json()['message'] == 'Incorrect password'

def test_login_user_not_found(client, init_database):
	response = client.post('/login', data=json.dumps({'email': 'notfound@example.com', 'password': 'testpassword'}), content_type='application/json')
	assert response.status_code == 404
	assert response.get_json()['message'] == 'User not found'
