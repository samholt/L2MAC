import pytest
from services.file_service import FileService

file_service = FileService()

@pytest.fixture

def setup():
	file = {'name': 'test.txt', 'path': '/path/to/test.txt', 'size': 100, 'type': 'text/plain'}
	user = 'test_user'
	file_service.upload_file(file, user)


def test_upload_file(setup):
	file = {'name': 'test.txt', 'path': '/path/to/test.txt', 'size': 100, 'type': 'text/plain'}
	user = 'test_user'
	new_file = file_service.upload_file(file, user)
	assert new_file['name'] == file['name']
	assert new_file['type'] == file['type']
	assert new_file['size'] == file['size']
	assert new_file['path'] == file['path']
	assert new_file['user'] == user
	assert new_file['tags'] == []
