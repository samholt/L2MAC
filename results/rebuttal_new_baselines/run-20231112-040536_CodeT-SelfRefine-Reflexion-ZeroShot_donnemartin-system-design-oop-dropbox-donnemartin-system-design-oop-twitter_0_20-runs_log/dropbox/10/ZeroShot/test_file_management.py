import pytest
import file_management

def test_upload():
	data = {'name': 'file.txt', 'type': 'text', 'size': 100, 'versions': []}
	response, status_code = file_management.upload(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download():
	data = {'name': 'file.txt'}
	response, status_code = file_management.download(data)
	assert status_code == 200
	assert response['name'] == 'file.txt'

def test_organize():
	data = {'name': 'file.txt', 'new_name': 'new_file.txt'}
	response, status_code = file_management.organize(data)
	assert status_code == 200
	assert response['message'] == 'File organized successfully'

def test_get_versions():
	response, status_code = file_management.get_versions()
	assert status_code == 200
	assert len(response) == 1

def test_restore_version():
	data = {'name': 'new_file.txt', 'version': 'v1'}
	response, status_code = file_management.restore_version(data)
	assert status_code == 200
	assert response['message'] == 'Version restored successfully'
