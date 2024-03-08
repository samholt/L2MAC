import pytest
import file_management

def test_upload_file():
	data = {'name': 'Test File', 'type': 'txt', 'size': 100, 'content': 'Hello, World!'}
	response = file_management.upload_file(data)
	assert response == {'message': 'File uploaded successfully'}

def test_download_file():
	data = {'name': 'Test File'}
	response = file_management.download_file(data)
	assert response == {'name': 'Test File', 'type': 'txt', 'size': 100, 'content': 'Hello, World!'}

def test_organize_file():
	data = {'name': 'Test File', 'new_name': 'New Test File'}
	response = file_management.organize_file(data)
	assert response == {'message': 'File organized successfully'}

def test_file_versioning():
	data = {'name': 'New Test File'}
	response = file_management.file_versioning(data)
	assert response == {'name': 'New Test File', 'type': 'txt', 'size': 100, 'content': 'Hello, World!'}
