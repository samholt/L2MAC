import pytest
import file_management

def test_upload():
	data = {'name': 'Test', 'size': 10, 'type': 'txt', 'versions': []}
	response = file_management.upload(data)
	assert response == {'message': 'File uploaded successfully'}


def test_download():
	data = {'name': 'Test'}
	response = file_management.download(data)
	assert 'name' in response


def test_organize():
	data = {'name': 'Test', 'new_name': 'NewTest'}
	response = file_management.organize(data)
	assert response == {'message': 'File organized successfully'}


def test_versioning():
	data = {'name': 'Test'}
	response = file_management.versioning(data)
	assert 'versions' in response
