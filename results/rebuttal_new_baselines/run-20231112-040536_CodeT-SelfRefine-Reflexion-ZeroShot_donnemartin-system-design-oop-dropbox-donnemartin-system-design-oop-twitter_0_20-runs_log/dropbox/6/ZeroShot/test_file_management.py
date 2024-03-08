import pytest
import file_management

def test_upload_file():
	data = {'name': 'Test', 'type': 'txt', 'size': 1, 'versions': []}
	response = file_management.upload_file(data)
	assert response == {'message': 'File uploaded successfully'}

def test_download_file():
	data = {'name': 'Test'}
	response = file_management.download_file(data)
	assert 'name' in response

def test_organize_file():
	data = {'name': 'Test', 'new_name': 'NewTest'}
	response = file_management.organize_file(data)
	assert response == {'message': 'File organized successfully'}

def test_version_file():
	data = {'name': 'Test'}
	response = file_management.version_file(data)
	assert 'versions' in response
