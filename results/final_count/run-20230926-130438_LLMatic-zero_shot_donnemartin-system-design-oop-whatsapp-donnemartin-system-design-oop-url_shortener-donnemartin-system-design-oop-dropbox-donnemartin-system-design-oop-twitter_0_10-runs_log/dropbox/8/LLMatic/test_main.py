import pytest
import main
from user_management import User
from file_management import File, Folder


def test_register():
	user = User('test', 'test@test.com', 'password')
	response = main.app.test_client().post('/register', json=user.__dict__)
	assert response.get_json()['message'] == 'Registration successful'


def test_login():
	response = main.app.test_client().post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.get_json()['message'] == 'Login successful'


def test_forgot_password():
	response = main.app.test_client().post('/forgot_password', json={'email': 'test@test.com'})
	assert response.get_json()['message'] == 'Password reset link sent'


def test_view_profile():
	user = User('test', 'test@test.com', 'password')
	response = main.app.test_client().get('/profile', json=user.__dict__)
	assert 'profile' in response.get_json()


def test_change_password():
	user = User('test', 'test@test.com', 'password')
	response = main.app.test_client().post('/change_password', json={'user': user.__dict__, 'new_password': 'new_password'})
	assert response.get_json()['message'] == 'Password changed successfully'


def test_upload_file():
	file = File('test.txt', 'txt', 100, 'test content', 1, '')
	response = main.app.test_client().post('/upload_file', json=file.__dict__)
	assert response.get_json()['message'] == 'File uploaded successfully'


def test_download_file():
	response = main.app.test_client().get('/download_file', json={'file_name': 'test.txt'})
	assert 'file' in response.get_json()


def test_generate_link():
	response = main.app.test_client().post('/generate_link', json={'file_or_folder': 'test.txt'})
	assert 'link' in response.get_json()


def test_invite_user():
	folder = Folder('test_folder', {})
	response = main.app.test_client().post('/invite_user', json={'folder': folder.__dict__, 'user': 'test@test.com'})
	assert response.get_json()['message'] == 'User invited'
