import pytest
import app
from db import db
from user import User
from post import Post

@pytest.fixture(autouse=True)
def setup():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		with app.app.app_context():
			db.create_all()
		yield client


def test_register(setup):
	response = setup.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()


def test_login(setup):
	response = setup.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == User(email='test@test.com', username='test', password='test').to_dict()


def test_create_post(setup):
	response = setup.post('/post', json={'user_email': 'test@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['user_email'] == 'test@test.com'
	assert response.get_json()['content'] == 'Hello, world!'
