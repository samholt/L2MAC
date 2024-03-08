import pytest
from app import app, users
from models import User, Transaction

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert '1' in users
	assert users['1'].username == 'test'
	assert users['1'].password == 'test'


def test_add_transaction(client):
	user = User(id='1', username='test', password='test')
	users[user.id] = user
	response = client.post('/add_transaction/1', json={'id': '1', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert len(users['1'].transactions) == 1
	assert users['1'].transactions[0].id == '1'
	assert users['1'].transactions[0].amount == 100.0
	assert users['1'].transactions[0].category == 'groceries'
