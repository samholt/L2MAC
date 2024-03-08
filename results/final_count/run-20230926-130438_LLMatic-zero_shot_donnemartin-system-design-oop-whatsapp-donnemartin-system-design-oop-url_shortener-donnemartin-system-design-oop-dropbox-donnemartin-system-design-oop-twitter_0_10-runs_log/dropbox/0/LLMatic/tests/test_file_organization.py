import pytest
from services.file_service import FileService

file_service = FileService()

@pytest.fixture

def setup_files():
	file_service.files = {}
	file_service.upload_file({'name': 'file1', 'type': 'txt', 'size': 100, 'path': ''}, 'user1')
	file_service.upload_file({'name': 'file2', 'type': 'txt', 'size': 200, 'path': ''}, 'user2')
	file_service.create_folder('folder1', 'user1')


def test_create_folder(setup_files):
	folder = file_service.create_folder('folder2', 'user2')
	assert folder['name'] == 'folder2'
	assert folder['type'] == 'folder'
	assert folder['user'] == 'user2'


def test_rename_file(setup_files):
	file = file_service.rename_file(1, 'new_file1')
	assert file['name'] == 'new_file1'


def test_move_file(setup_files):
	file = file_service.move_file(2, 'folder1')
	assert file['path'] == 'folder1'


def test_delete_file(setup_files):
	message = file_service.delete_file(3)
	assert message == 'File deleted'
	assert 3 not in file_service.files
