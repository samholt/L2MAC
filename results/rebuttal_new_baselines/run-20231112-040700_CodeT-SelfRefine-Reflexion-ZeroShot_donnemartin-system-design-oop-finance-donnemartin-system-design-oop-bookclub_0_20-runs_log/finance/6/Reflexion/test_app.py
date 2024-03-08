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
	assert 'test' in app.users


def test_add_transaction(client):
	app.users['test'] = app.User('test', 'test')
	response = client.post('/add_transaction', json={'user': 'test', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}
	assert 'test' in app.transactions
