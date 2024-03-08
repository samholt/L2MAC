import pytest
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'


def test_create_transaction(client):
	response = client.post('/transaction', json={'user': 'test', 'amount': 100, 'type': 'debit', 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Transaction created successfully'


def test_set_budget(client):
	response = client.post('/budget', json={'user': 'test', 'amount': 1000, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Budget set successfully'


def test_link_investment(client):
	response = client.post('/investment', json={'user': 'test', 'type': 'stocks', 'amount': 10000, 'performance': 10, 'account': '123456'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Investment account linked successfully'


def test_set_alert(client):
	response = client.post('/alert', json={'user': 'test', 'alert_type': 'budget', 'message': 'Budget limit nearing'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Alert set and sent successfully'
