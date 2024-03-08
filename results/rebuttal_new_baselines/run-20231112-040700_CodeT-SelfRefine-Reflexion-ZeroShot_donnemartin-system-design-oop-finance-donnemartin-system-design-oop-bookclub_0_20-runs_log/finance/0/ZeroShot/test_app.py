import pytest
import app
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert app.users_db['test'].username == 'test'
	assert app.users_db['test'].password == hashlib.sha256('test'.encode()).hexdigest()

def test_login(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

def test_add_transaction(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	response = client.post('/transaction', json={'username': 'test', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 201
	assert len(app.transactions_db['test']) == 1
	assert app.transactions_db['test'][0].user == 'test'
	assert app.transactions_db['test'][0].category == 'groceries'
	assert app.transactions_db['test'][0].amount == 100.0

def test_get_transactions(client):
	client.post('/register', json={'username': 'test', 'password': 'test'})
	client.post('/transaction', json={'username': 'test', 'category': 'groceries', 'amount': 100.0})
	response = client.get('/transactions', query_string={'username': 'test'})
	assert response.status_code == 200
	assert len(response.get_json()) == 1
	assert response.get_json()[0]['user'] == 'test'
	assert response.get_json()[0]['category'] == 'groceries'
	assert response.get_json()[0]['amount'] == 100.0
