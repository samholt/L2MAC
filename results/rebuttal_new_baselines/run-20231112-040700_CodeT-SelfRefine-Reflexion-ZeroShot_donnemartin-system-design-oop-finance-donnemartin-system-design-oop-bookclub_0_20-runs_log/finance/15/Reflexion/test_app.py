import pytest
import app

@pytest.fixture(autouse=True)
def clear_data():
	app.users.clear()
	app.transactions.clear()

def test_register():
	response = app.app.test_client().post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	response = app.app.test_client().post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

def test_login():
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	app.app.test_client().post('/register', json={'username': 'test', 'password': 'test'})
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

def test_add_transaction():
	response = app.app.test_client().post('/transactions', json={'username': 'test', 'transaction': 'test'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User does not exist'}

	app.app.test_client().post('/register', json={'username': 'test', 'password': 'test'})
	response = app.app.test_client().post('/transactions', json={'username': 'test', 'transaction': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}

def test_get_transactions():
	response = app.app.test_client().get('/transactions', query_string={'username': 'test'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User does not exist'}

	app.app.test_client().post('/register', json={'username': 'test', 'password': 'test'})
	response = app.app.test_client().get('/transactions', query_string={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'transactions': []}

	app.app.test_client().post('/transactions', json={'username': 'test', 'transaction': 'test'})
	response = app.app.test_client().get('/transactions', query_string={'username': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'transactions': ['test']}
