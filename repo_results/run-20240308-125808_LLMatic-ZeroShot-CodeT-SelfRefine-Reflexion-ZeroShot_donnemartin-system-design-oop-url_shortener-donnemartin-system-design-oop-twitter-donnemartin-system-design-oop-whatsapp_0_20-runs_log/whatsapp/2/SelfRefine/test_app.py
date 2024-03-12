import pytest
import json
from app import app, db, User

@pytest.fixture(scope='module')
def test_client():
	app.config['TESTING'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.test_client() as testing_client:
		with app.app_context():
			db.create_all()
			yield testing_client  
			db.session.remove()
			db.drop_all()


def test_signup(test_client):
	response = test_client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_login(test_client):
	response = test_client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_logout(test_client):
	response = test_client.post('/logout', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged out successfully'}


def test_forgot_password(test_client):
	response = test_client.post('/forgot_password', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Password reset successfully'}
