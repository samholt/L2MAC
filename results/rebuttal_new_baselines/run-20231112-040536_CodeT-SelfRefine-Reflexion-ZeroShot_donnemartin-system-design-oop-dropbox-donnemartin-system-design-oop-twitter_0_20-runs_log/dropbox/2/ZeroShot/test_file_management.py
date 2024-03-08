import pytest
import file_management

def test_upload():
	data = {'name': 'test.txt', 'size': 100, 'type': 'text/plain'}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'test.txt'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert 'file' in response

def test_organize():
	data = {'name': 'test.txt', 'new_name': 'new_test.txt'}
	response, status_code = file_management.organize(data)
	assert status_code == 200
	assert response['message'] == 'File organized successfully'

def test_get_versions():
	response, status_code = file_management.get_versions()
	assert status_code == 200
	assert 'files' in response

def test_restore_version():
	data = {'name': 'test.txt', 'versions': ['v1', 'v2']}
	response, status_code = file_management.restore_version(data)
	assert status_code == 200
	assert response['message'] == 'File version restored successfully'
