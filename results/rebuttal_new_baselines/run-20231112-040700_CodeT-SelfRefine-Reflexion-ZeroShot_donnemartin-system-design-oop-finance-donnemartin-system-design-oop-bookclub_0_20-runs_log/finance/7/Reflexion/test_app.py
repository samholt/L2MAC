import pytest
import json
from app import app, User, Transaction

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}

def test_add_transaction(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_transaction', json={'username': 'test', 'category': 'groceries', 'amount': 100.0})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Transaction added successfully'}

def test_view_transactions(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	client.post('/add_transaction', json={'username': 'test', 'category': 'groceries', 'amount': 100.0})
	response = client.get('/view_transactions', query_string={'username': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'username': 'test', 'category': 'groceries', 'amount': 100.0}
