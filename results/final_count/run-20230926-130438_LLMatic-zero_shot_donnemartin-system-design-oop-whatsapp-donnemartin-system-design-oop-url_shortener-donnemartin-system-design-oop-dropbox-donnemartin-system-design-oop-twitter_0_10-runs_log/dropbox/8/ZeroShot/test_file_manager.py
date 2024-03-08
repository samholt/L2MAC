import pytest
from file_manager import FileManager

def test_upload():
	file_manager = FileManager()
	response = file_manager.upload({'file': {'name': 'test.txt', 'content': 'Hello, World!'}})
	assert response['status'] == 'success'
	assert response['message'] == 'File uploaded successfully'

	response = file_manager.upload({})
	assert response['status'] == 'error'
	assert response['message'] == 'No file provided'}

def test_download():
	file_manager = FileManager()
	file_manager.upload({'file': {'name': 'test.txt', 'content': 'Hello, World!'}})

	response = file_manager.download({'file_name': 'test.txt'})
	assert response['status'] == 'success'
	assert response['message'] == 'File downloaded successfully'
	assert response['file']['name'] == 'test.txt'
	assert response['file']['content'] == 'Hello, World!'

	response = file_manager.download({'file_name': 'nonexistent.txt'})
	assert response['status'] == 'error'
	assert response['message'] == 'File not found'

	response = file_manager.download({})
	assert response['status'] == 'error'
	assert response['message'] == 'No file name provided'}
