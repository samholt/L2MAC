import pytest
import file_management

def test_upload_file():
	data = {'name': 'Test', 'size': 100, 'type': 'txt', 'versions': []}
	response = file_management.upload_file(data)
	assert response == {'message': 'File uploaded successfully'}

def test_download_file():
	data = {'name': 'Test'}
	response = file_management.download_file(data)
	assert 'name' in response and 'size' in response and 'type' in response and 'versions' in response
def test_organize_file():
	data = {'name': 'Test', 'new_name': 'NewTest'}
	response = file_management.organize_file(data)
	assert response == {'message': 'File organized successfully'}

def test_file_versioning():
	data = {'name': 'NewTest'}
	response = file_management.file_versioning(data)
	assert 'versions' in response
