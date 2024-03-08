import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid credentials'}

	response = client.post('/message', json={'from_user': 'test@test.com', 'to_user': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Message sent'}

	response = client.get('/message?from_user=test@test.com&to_user=test2@test.com')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1
