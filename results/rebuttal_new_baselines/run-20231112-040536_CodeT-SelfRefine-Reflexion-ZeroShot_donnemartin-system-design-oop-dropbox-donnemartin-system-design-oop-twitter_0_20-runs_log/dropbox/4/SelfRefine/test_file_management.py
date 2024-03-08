import pytest
import file_management
from db import db
from app import app

def setup_function():
	with app.app_context():
		db.create_all()

def teardown_function():
	with app.app_context():
		db.session.remove()
		db.drop_all()

def test_upload():
	data = {'name': 'Test File', 'type': 'txt', 'size': 100}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'Test File'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert response['message'] == 'File download endpoint'
