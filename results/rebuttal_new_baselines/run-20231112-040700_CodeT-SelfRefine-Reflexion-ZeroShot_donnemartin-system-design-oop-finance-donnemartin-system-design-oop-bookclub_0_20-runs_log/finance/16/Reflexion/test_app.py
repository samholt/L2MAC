import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_login(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Login successful'}


def test_set_budget(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/set_budget', json={'username': 'test', 'budget': 1000.0})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Budget set successfully'}


def test_add_income(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_income', json={'username': 'test', 'income': 500.0})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Income added successfully'}


def test_add_expense(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	response = client.post('/add_expense', json={'username': 'test', 'expense': 200.0})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Expense added successfully'}


def test_generate_report(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test'})
	client.post('/set_budget', json={'username': 'test', 'budget': 1000.0})
	client.post('/add_income', json={'username': 'test', 'income': 500.0})
	client.post('/add_expense', json={'username': 'test', 'expense': 200.0})
	response = client.get('/generate_report?username=test')
	assert response.status_code == 200
	assert json.loads(response.data) == {
		'username': 'test',
		'budget': 1000.0,
		'income': 500.0,
		'expenses': 200.0,
		'remaining_budget': 800.0
	}
