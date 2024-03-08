import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register_login(client):
	response = client.post('/register', json={'username': 'test_user', 'password': 'test_password', 'email': 'test_email'})
	assert response.status_code == 201
	response = client.post('/login', json={'username': 'test_user', 'password': 'test_password'})
	assert response.status_code == 200
	verification_code = response.headers['X-Verification-Code']
	response = client.post('/verify', json={'username': 'test_user', 'code': verification_code})
	assert response.status_code == 200


def test_add_investment(client):
	response = client.post('/investment', json={'username': 'test_user', 'password': 'test_password', 'account_name': 'test', 'balance': 1000, 'asset_allocation': '50-50'})
	assert response.status_code == 201


def test_update_investment(client):
	response = client.put('/investment', json={'username': 'test_user', 'password': 'test_password', 'account_name': 'test', 'new_balance': 2000, 'new_asset_allocation': '60-40'})
	assert response.status_code == 200


def test_delete_investment(client):
	response = client.delete('/investment', json={'username': 'test_user', 'password': 'test_password', 'account_name': 'test'})
	assert response.status_code == 200


def test_invalid_credentials(client):
	response = client.post('/investment', json={'username': 'wrong_user', 'password': 'wrong_password', 'account_name': 'test', 'balance': 1000, 'asset_allocation': '50-50'})
	assert response.status_code == 401
	response = client.put('/investment', json={'username': 'wrong_user', 'password': 'wrong_password', 'account_name': 'test', 'new_balance': 2000, 'new_asset_allocation': '60-40'})
	assert response.status_code == 401
	response = client.delete('/investment', json={'username': 'wrong_user', 'password': 'wrong_password', 'account_name': 'test'})
	assert response.status_code == 401
