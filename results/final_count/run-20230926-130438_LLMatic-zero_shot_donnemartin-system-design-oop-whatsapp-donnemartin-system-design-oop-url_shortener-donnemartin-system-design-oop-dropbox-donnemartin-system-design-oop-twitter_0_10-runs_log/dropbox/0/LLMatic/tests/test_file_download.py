import pytest
from services.file_service import FileService
from models.File import File

file_service = FileService()

@pytest.fixture

def setup():
	file = {'name': 'test_file', 'type': 'txt', 'size': 100, 'path': '/path/to/file'}
	user = 'test_user'
	file_service.upload_file(file, user)


def test_file_download(setup):
	file_id = 1
	file = file_service.download_file(file_id)
	assert file['id'] == file_id
	assert file['name'] == 'test_file'
	assert file['type'] == 'txt'
	assert file['size'] == 100
	assert file['path'] == '/path/to/file'
	assert file['user'] == 'test_user'
	assert file['tags'] == []
