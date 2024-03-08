import pytest
from cloudsafe.app.models import User, File, Folder


def test_user_model():
	user = User(1, 'Test User', 'test@example.com', 'password', 'http://example.com/profile.jpg')
	assert user.id == 1
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.profile_picture == 'http://example.com/profile.jpg'
	assert user.check_password('password')


def test_file_model():
	file = File(1, 'Test File', 1)
	assert file.id == 1
	assert file.name == 'Test File'
	assert file.user_id == 1
	assert file.folder_id is None


def test_folder_model():
	folder = Folder(1, 'Test Folder', 1)
	assert folder.id == 1
	assert folder.name == 'Test Folder'
	assert folder.user_id == 1
	assert folder.parent_folder_id is None

