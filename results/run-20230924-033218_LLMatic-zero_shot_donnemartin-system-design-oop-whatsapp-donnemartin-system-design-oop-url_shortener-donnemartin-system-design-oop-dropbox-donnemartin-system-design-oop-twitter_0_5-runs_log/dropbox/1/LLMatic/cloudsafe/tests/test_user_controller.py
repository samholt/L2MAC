import pytest
from flask import Flask
from cloudsafe.app.user_controller import user_blueprint

@pytest.fixture

def create_app():
	app = Flask(__name__)
	app.register_blueprint(user_blueprint)
	return app

def test_register_user(create_app):
	client = create_app.test_client()
	response = client.post('/register', json={'id': '1', 'name': 'Test User', 'email': 'test@example.com', 'password': 'password', 'profile_picture': 'picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login_user(create_app):
	client = create_app.test_client()
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}

def test_change_password(create_app):
	client = create_app.test_client()
	response = client.put('/change_password', json={'email': 'test@example.com', 'old_password': 'password', 'new_password': 'new_password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password changed successfully'}

def test_update_profile_picture(create_app):
	client = create_app.test_client()
	response = client.put('/update_profile_picture', json={'email': 'test@example.com', 'new_profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated successfully'}
