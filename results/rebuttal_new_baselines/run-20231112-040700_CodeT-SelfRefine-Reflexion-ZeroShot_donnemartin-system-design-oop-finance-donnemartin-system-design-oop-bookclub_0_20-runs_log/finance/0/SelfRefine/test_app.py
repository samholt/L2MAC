import pytest
import app
from flask import json

@pytest.fixture(scope='module')
def test_client():
	app.app.config['TESTING'] = True
	app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	test_client = app.app.test_client()

	with app.app.app_context():
		# Create the database and the database table
		app.db.create_all()

	yield test_client  # this is where the testing happens!

	with app.app.app_context():
		# After the test, drop all tables in the database
		app.db.session.remove()
		app.db.drop_all()


def test_create_user(test_client):
	data = {'id': '1', 'username': 'test', 'password': 'test'}
	response = test_client.post('/create_user', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data['id']


def test_add_transaction(test_client):
	data = {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'}
	response = test_client.post('/add_transaction', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data['id']
