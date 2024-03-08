import pytest
import app
import sqlite3

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

	# Check if user is in the database
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	c.execute("SELECT * FROM users WHERE username='test'")
	user = c.fetchone()
	assert user is not None

	# Try to create the same user again
	response = client.post('/create_user', json={'username': 'test', 'password': 'test123'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}


def test_add_transaction(client):
	response = client.post('/add_transaction', json={'user_id': 'test', 'type': 'income', 'amount': 1000.0, 'category': 'salary'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Transaction added successfully'}

	# Check if transaction is in the database
	c.execute("SELECT * FROM transactions WHERE user_id='test'")
	transaction = c.fetchone()
	assert transaction is not None

	# Try to add a transaction for a non-existent user
	response = client.post('/add_transaction', json={'user_id': 'nonexistent', 'type': 'income', 'amount': 1000.0, 'category': 'salary'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User does not exist'}
