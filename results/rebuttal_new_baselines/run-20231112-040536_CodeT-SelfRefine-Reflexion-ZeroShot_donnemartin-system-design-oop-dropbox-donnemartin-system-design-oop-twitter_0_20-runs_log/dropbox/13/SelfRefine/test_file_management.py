import pytest
import file_management

def test_upload_file():
	data = {'name': 'test.txt', 'type': 'text', 'size': 1, 'versions': ['v1']}
	response = file_management.upload_file(data)
	assert response == {'message': 'File uploaded successfully'}

def test_download_file():
	data = {'name': 'test.txt'}
	response = file_management.download_file(data)
	assert 'name' in response

def test_organize_file():
	data = {'name': 'test.txt', 'new_name': 'new_test.txt'}
	response = file_management.organize_file(data)
	assert response == {'message': 'File organized successfully'}

def test_versioning():
	data = {'name': 'test.txt', 'type': 'text', 'size': 1, 'versions': ['v1']}
	file_management.upload_file(data)
	data = {'name': 'test.txt'}
	response = file_management.versioning(data)
	assert 'versions' in response
	assert response['versions'] == ['v1']
