import pytest
from app import app, db
from models import User


def setup_module():
	with app.app_context():
		db.create_all()


def teardown_module():
	with app.app_context():
		db.session.remove()
		db.drop_all()


def test_register():
	with app.app_context():
		response = app.test_client().post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert response.status_code == 201
		assert response.get_json() == {'message': 'registered successfully'}


def test_login():
	with app.app_context():
		response = app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert 'token' in response.get_json()


def test_login_fail():
	with app.app_context():
		response = app.test_client().post('/login', json={'username': 'test', 'password': 'wrong'})
		assert response.status_code == 400
