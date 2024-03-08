import pytest
from app import app


def test_register_user():
	with app.test_client() as c:
		response = c.post('/register', json={'name': 'test', 'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_login_user():
	with app.test_client() as c:
		response = c.post('/login', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_reset_password():
	with app.test_client() as c:
		response = c.post('/forgot_password', json={'email': 'test@test.com', 'new_password': 'new_test'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_get_profile():
	with app.test_client() as c:
		response = c.get('/profile', query_string={'email': 'test@test.com'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_update_password():
	with app.test_client() as c:
		response = c.post('/change_password', json={'email': 'test@test.com', 'new_password': 'new_test'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_upload_file():
	with app.test_client() as c:
		response = c.post('/upload', json={'name': 'test', 'type': 'text', 'size': 4, 'content': 'test', 'folder_name': 'test_folder'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_download_file():
	with app.test_client() as c:
		response = c.get('/download', query_string={'file_name': 'test', 'folder_name': 'test_folder'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_create_folder():
	with app.test_client() as c:
		response = c.post('/create_folder', json={'name': 'test_folder'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_move_file():
	with app.test_client() as c:
		response = c.post('/move_file', json={'file_name': 'test', 'folder_name': 'test_folder'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_share_file():
	with app.test_client() as c:
		response = c.post('/share_file', json={'file_name': 'test', 'email': 'test@test.com'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_encrypt_file():
	with app.test_client() as c:
		response = c.post('/encrypt_file', json={'file_name': 'test'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'


def test_log_activity():
	with app.test_client() as c:
		response = c.post('/log_activity', json={'user_email': 'test@test.com', 'activity': 'test_activity'})
		assert response.status_code == 200
		assert response.json['status'] == 'success'

