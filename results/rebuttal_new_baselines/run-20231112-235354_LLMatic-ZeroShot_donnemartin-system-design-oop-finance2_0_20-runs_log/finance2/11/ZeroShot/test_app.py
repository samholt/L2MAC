import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}
