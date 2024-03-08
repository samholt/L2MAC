import pytest
import app
from app import User, Transaction

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	user = User(id='1', username='test', password='test')
	response = client.post('/create_user', json=user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == user.__dict__


def test_add_transaction(client):
	transaction = Transaction(id='1', user_id='1', amount=100.0, category='groceries')
	response = client.post('/add_transaction', json=transaction.__dict__)
	assert response.status_code == 201
	assert response.get_json() == transaction.__dict__
