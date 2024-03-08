import pytest
import user_management
from db import db
from app import app

def setup_function():
	with app.app_context():
		db.create_all()

def teardown_function():
	with app.app_context():
		db.session.remove()
		db.drop_all()

def test_register():
	data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}
	response, status_code = user_management.register(data)
	assert status_code == 201
	assert response['message'] == 'User registered successfully'

def test_login():
	data = {'email': 'test@example.com', 'password': 'password'}
	response, status_code = user_management.login(data)
	assert status_code == 200
	assert response['message'] == 'Login successful'

def test_forgot_password():
	data = {'email': 'test@example.com', 'new_password': 'new_password'}
	response, status_code = user_management.forgot_password(data)
	assert status_code == 200
	assert response['message'] == 'Password updated successfully'
