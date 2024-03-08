import pytest
import file_management

def test_upload_file():
	data = {'name': 'test.txt', 'size': 100, 'type': 'text/plain', 'location': '/'}
	response, status_code = file_management.upload_file(data)
	assert status_code == 201
	assert response['message'] == 'File uploaded successfully'

def test_download_file():
	data = {'name': 'test.txt'}
	response, status_code = file_management.download_file(data)
	assert status_code == 200
	assert 'file' in response

def test_create_folder():
	data = {'name': 'test_folder'}
	response, status_code = file_management.create_folder(data)
	assert status_code == 201
	assert response['message'] == 'Folder created successfully'

def test_rename_file():
	data = {'old_name': 'test.txt', 'new_name': 'new_test.txt'}
	response, status_code = file_management.rename_file(data)
	assert status_code == 200
	assert response['message'] == 'File renamed successfully'

def test_move_file():
	data = {'name': 'new_test.txt', 'new_location': '/test_folder'}
	response, status_code = file_management.move_file(data)
	assert status_code == 200
	assert response['message'] == 'File moved successfully'

def test_delete_file():
	data = {'name': 'new_test.txt'}
	response, status_code = file_management.delete_file(data)
	assert status_code == 200
	assert response['message'] == 'File deleted successfully'
