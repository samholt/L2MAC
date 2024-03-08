import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_account(client):
	response = client.post('/create_account', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Account created successfully'}

	# Test creating account with existing username
	response = client.post('/create_account', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}
