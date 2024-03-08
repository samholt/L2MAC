import pytest
from models.folder import Folder
from models.user import User


def test_folder_model():
	user = User('Test User', 'test@example.com', 'password')
	folder = Folder('Test Folder', '/path/to/folder', user)

	assert folder.get_id() is None
	assert folder.get_name() == 'Test Folder'
	assert folder.get_path() == '/path/to/folder'
	assert folder.get_owner() == user
	assert folder.get_files() == []

	folder.set_name('New Folder Name')
	folder.set_path('/new/path/to/folder')
	folder.set_owner(None)
	folder.set_files(None)

	assert folder.get_name() == 'New Folder Name'
	assert folder.get_path() == '/new/path/to/folder'
	assert folder.get_owner() is None
	assert folder.get_files() is None
