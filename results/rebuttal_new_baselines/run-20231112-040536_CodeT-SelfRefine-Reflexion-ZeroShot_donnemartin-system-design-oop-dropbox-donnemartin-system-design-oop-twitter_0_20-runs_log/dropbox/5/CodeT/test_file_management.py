import pytest
import file_management

def test_upload():
	data = {'name': 'file.txt', 'type': 'text', 'size': 10, 'content': 'Hello, World!', 'versions': []}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'file.txt'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert 'file' in response

def test_organize():
	data = {'name': 'file.txt', 'new_name': 'new_file.txt'}
	response, status_code = file_management.organize(data)
	assert status_code == 200
	assert response['message'] == 'File organized successfully'

def test_get_version():
	response, status_code = file_management.get_version()
	assert status_code == 200
	assert len(response) == 1

def test_update_version():
	data = {'name': 'new_file.txt', 'new_version': 'v2'}
	response, status_code = file_management.update_version(data)
	assert status_code == 200
	assert response['message'] == 'Version updated successfully'
