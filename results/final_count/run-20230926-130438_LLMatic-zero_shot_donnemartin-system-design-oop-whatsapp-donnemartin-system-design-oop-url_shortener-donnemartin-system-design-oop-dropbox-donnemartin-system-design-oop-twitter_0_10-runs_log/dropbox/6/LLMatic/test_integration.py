import pytest
from main import app
from user_management.routes import mock_db, User
from file_management.routes import files_db, File
from file_sharing.routes import share_links
from security.routes import activity_log
from flask import json
from io import BytesIO

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_integration(client):
	# Test user registration
	response = client.post('/register', data={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'Registration successful' in response.get_data(as_text=True)
	assert 'test@example.com' in mock_db

	# Test file upload
	response = client.post('/upload', data={'file': (BytesIO(b'test content'), 'test.txt')}, content_type='multipart/form-data')
	assert response.status_code == 200
	assert 'File uploaded successfully' in response.get_data(as_text=True)
	assert 'test.txt' in files_db

	# Test file sharing
	response = client.post('/share', data=json.dumps({'file_id': 'test.txt'}), content_type='application/json')
	assert response.status_code == 200
	assert 'link_id' in response.get_json()
	link_id = response.get_json()['link_id']
	assert link_id in share_links

	# Test file encryption
	response = client.post('/encrypt', data=json.dumps({'file': 'test content'}), content_type='application/json')
	assert response.status_code == 200
	assert 'encrypted_file' in response.get_json()
	assert {'action': 'encrypt', 'file': 'test content'} in activity_log

	# Test file deletion
	response = client.get('/delete_file/test.txt')
	assert response.status_code == 200
	assert 'File deleted successfully' in response.get_data(as_text=True)
	assert 'test.txt' not in files_db
