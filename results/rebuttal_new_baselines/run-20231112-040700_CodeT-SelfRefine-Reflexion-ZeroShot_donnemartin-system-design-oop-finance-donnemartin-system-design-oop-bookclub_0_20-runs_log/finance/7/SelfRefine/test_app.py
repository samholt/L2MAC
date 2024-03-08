import pytest
import app
import json
from app import db, User, Transaction

@pytest.fixture(scope='module')
def test_client():
	app.app.config['TESTING'] = True
	app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.app.test_client() as testing_client:
		with app.app.app_context():
			db.create_all()
		yield testing_client
		db.session.remove()
		db.drop_all()


def test_create_user(test_client):
	response = test_client.post('/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'username': 'test', 'password': 'test'}
	user_in_db = User.query.get('1')
	assert user_in_db is not None


def test_add_transaction(test_client):
	response = test_client.post('/add_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'}
	transaction_in_db = Transaction.query.get('1')
	assert transaction_in_db is not None
