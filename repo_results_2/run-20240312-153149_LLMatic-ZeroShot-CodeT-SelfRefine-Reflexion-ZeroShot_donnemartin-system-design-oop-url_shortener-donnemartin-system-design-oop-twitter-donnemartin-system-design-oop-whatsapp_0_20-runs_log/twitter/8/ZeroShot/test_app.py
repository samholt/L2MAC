import pytest
from app import app, db
from models import User, Post


def setup_module():
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	app.config['TESTING'] = True
	with app.app_context():
		db.create_all()


def teardown_module():
	with app.app_context():
		db.drop_all()


def test_register():
	with app.test_client() as client:
		res = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert res.status_code == 201
		assert 'Registered successfully' in res.get_json()['message']


def test_login():
	with app.test_client() as client:
		res = client.post('/login', json={'username': 'test', 'password': 'test'})
		assert res.status_code == 200
		assert 'access_token' in res.get_json()


def test_create_post():
	with app.test_client() as client:
		res = client.post('/login', json={'username': 'test', 'password': 'test'})
		access_token = res.get_json()['access_token']
		res = client.post('/post', json={'content': 'Hello, world!'}, headers={'Authorization': 'Bearer ' + access_token})
		assert res.status_code == 201
		assert 'Post created' in res.get_json()['message']
