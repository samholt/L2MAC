import pytest
from flask import Flask
from werkzeug.datastructures import FileStorage
from cloudsafe.app import app, File, files_db
import os

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def sample_file():
	file_obj = FileStorage(stream=open('cloudsafe/tests/test_file.txt', 'rb'), filename='test_file.txt')
	return file_obj

@pytest.fixture
def uploaded_file(client, sample_file):
	data = {
		'name': 'test_file.txt',
		'size': 20,
		'type': 'text',
		'user_id': 1
	}
	os.makedirs('uploads', exist_ok=True)
	response = client.post('/upload', data={'file': sample_file, 'data': data}, content_type='multipart/form-data')
	file_id = response.json['file_id']
	files_db[file_id] = File(
		id=file_id,
		name='test_file.txt',
		size=20,
		type='text',
		path='uploads/test_file.txt',
		user_id=1
	)
	return file_id


def test_download(client, uploaded_file):
	response = client.get(f'/download?id={uploaded_file}')
	assert response.status_code == 200
	assert response.data == b'This is a test file for CloudSafe.'

