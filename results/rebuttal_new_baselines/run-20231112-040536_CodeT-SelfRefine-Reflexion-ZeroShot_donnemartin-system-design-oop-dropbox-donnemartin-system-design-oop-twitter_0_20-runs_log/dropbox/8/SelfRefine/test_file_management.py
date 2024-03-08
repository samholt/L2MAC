import pytest
import file_management

def test_upload():
	data = {'name': 'test.txt', 'type': 'text', 'size': 10, 'content': 'Test content', 'versions': ['v1']}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'test.txt'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert response['file']['name'] == 'test.txt'

def test_organize():
	data = {'name': 'test.txt', 'new_name': 'new_test.txt'}
	response, status_code = file_management.organize(data)
	assert status_code == 200
	assert response['message'] == 'File organized successfully'

def test_get_version():
	response, status_code = file_management.get_version()
	assert status_code == 200
	assert len(response) == 1

def test_update_version():
	data = {'name': 'new_test.txt', 'new_version': 'v2'}
	response, status_code = file_management.update_version(data)
	assert status_code == 200
	assert response['message'] == 'Version updated successfully'
