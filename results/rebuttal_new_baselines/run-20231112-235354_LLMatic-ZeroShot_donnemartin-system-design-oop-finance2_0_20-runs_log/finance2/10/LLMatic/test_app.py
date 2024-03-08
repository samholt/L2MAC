import pytest
from app import app
from models.user import User


def test_register():
	with app.test_client() as client:
		response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 201


def test_login():
	with app.test_client() as client:
		response = client.post('/login', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200


def test_verify():
	user = User('test', 'test@test.com', 'test')
	user.generate_verification_code()
	with app.test_client() as client:
		response = client.post('/verify', json={'username': 'test', 'email': 'test@test.com', 'password': 'test', 'verification_code': user.verification_code})
		assert response.status_code == 200


def test_link_bank_account():
	with app.test_client() as client:
		response = client.post('/link_bank_account', json={'username': 'test', 'email': 'test@test.com', 'password': 'test', 'bank_account': '1234567890'})
		assert response.status_code == 200
		user = User('test', 'test@test.com', 'test')
		assert user.link_bank_account('1234567890') == '1234567890'
