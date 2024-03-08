import pytest
import app
import json


def test_register():
	with app.app.test_client() as c:
		response = c.post('/register', json={'name': 'test', 'email': 'test@test.com', 'password': 'test123'})
		assert response.status_code == 200


def test_login():
	with app.app.test_client() as c:
		response = c.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
		assert response.status_code == 200


def test_forgot_password():
	with app.app.test_client() as c:
		response = c.post('/forgot_password', json={'email': 'test@test.com'})
		assert response.status_code == 200


def test_profile():
	with app.app.test_client() as c:
		response = c.get('/profile', json={'email': 'test@test.com'})
		assert response.status_code == 200


def test_change_password():
	with app.app.test_client() as c:
		response = c.post('/change_password', json={'email': 'test@test.com', 'old_password': 'test123', 'new_password': 'test1234'})
		assert response.status_code == 200


def test_upload():
	with app.app.test_client() as c:
		response = c.post('/upload', json={'file': 'test_file', 'email': 'test@test.com'})
		assert response.status_code == 200


def test_download():
	with app.app.test_client() as c:
		response = c.get('/download', json={'file_name': 'test_file', 'email': 'test@test.com', 'version_number': 1})
		assert response.status_code == 200


def test_share():
	with app.app.test_client() as c:
		response = c.post('/share', json={'file_path': 'test_file', 'expiry_date': '2022-12-31', 'password': 'test123'})
		assert response.status_code == 200


def test_get_shared_file():
	with app.app.test_client() as c:
		response = c.get('/get_shared_file', json={'share_id': 1, 'password': 'test123'})
		assert response.status_code == 200


def test_encrypt():
	with app.app.test_client() as c:
		response = c.post('/encrypt', json={'data': 'test_data'})
		assert response.status_code == 200


def test_decrypt():
	with app.app.test_client() as c:
		response = c.post('/decrypt', json={'data': 'test_data'})
		assert response.status_code == 200


def test_switch_theme():
	with app.app.test_client() as c:
		response = c.post('/switch_theme', json={'theme': 'dark'})
		assert response.status_code == 200


def test_adjust_screen_size():
	with app.app.test_client() as c:
		response = c.post('/adjust_screen_size', json={'screen_size': '1024x768'})
		assert response.status_code == 200


def test_preview_file():
	with app.app.test_client() as c:
		response = c.get('/preview_file', json={'file': 'test_file'})
		assert response.status_code == 200

