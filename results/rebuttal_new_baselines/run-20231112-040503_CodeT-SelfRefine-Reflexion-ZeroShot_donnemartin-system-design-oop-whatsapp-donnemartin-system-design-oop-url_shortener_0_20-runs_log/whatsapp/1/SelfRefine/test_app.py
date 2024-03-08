import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return {'email': 'test@test.com', 'password': 'test'}

def test_signup(client, user):
	response = client.post('/signup', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'

	response = client.post('/signup', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Email already exists'

def test_login_logout(client, user):
	response = client.post('/login', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Invalid email or password'

	client.post('/signup', data=json.dumps(user), content_type='application/json')

	response = client.post('/login', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

	response = client.post('/login', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User already logged in'

	response = client.post('/logout', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged out successfully'

	response = client.post('/logout', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User not logged in'
