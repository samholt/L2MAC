import pytest
import file_management

def test_upload_file():
	data = {'name': 'Test File', 'type': 'txt', 'size': 100, 'content': 'This is a test file'}
	response = file_management.upload_file(data)
	assert response['status'] == 'success'
	assert response['message'] == 'File uploaded successfully'

def test_download_file():
	data = {'name': 'Test File'}
	response = file_management.download_file(data)
	assert response['status'] == 'success'
	assert response['data']['name'] == 'Test File'
	assert response['data']['type'] == 'txt'
	assert response['data']['size'] == 100
	assert response['data']['content'] == 'This is a test file'

def test_organize_file():
	data = {'name': 'Test File', 'new_name': 'New Test File'}
	response = file_management.organize_file(data)
	assert response['status'] == 'success'
	assert response['message'] == 'File organized successfully'

def test_file_versioning():
	data = {'name': 'New Test File'}
	response = file_management.file_versioning(data)
	assert response['status'] == 'success'
	assert response['data']['name'] == 'New Test File'
	assert response['data']['type'] == 'txt'
	assert response['data']['size'] == 100
	assert response['data']['content'] == 'This is a test file'
	assert response['data']['version'] == 2
