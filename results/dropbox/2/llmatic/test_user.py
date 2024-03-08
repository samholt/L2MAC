import pytest
from user import User
from file import File

def test_user_creation():
	user = User('test_user', 'password')
	assert user.username == 'test_user'
	assert user.password == 'password'

def test_upload_file():
	user = User('test_user', 'password')
	file = File('test_file', 100, 'Hello, World!')
	file_id = user.upload_file(file)
	assert file_id == 0

def test_view_file():
	user = User('test_user', 'password')
	file = File('test_file', 100, 'Hello, World!')
	file_id = user.upload_file(file)
	content = user.view_file(file_id)
	assert content == 'Hello, World!'

def test_search_file():
	user = User('test_user', 'password')
	file = File('test_file', 100, 'Hello, World!')
	file_id = user.upload_file(file)
	found_file_id = user.search_file('test_file')
	assert found_file_id == file_id

def test_share_file():
	user1 = User('test_user1', 'password')
	user2 = User('test_user2', 'password')
	file = File('test_file', 100, 'Hello, World!')
	file_id = user1.upload_file(file)
	user1.share_file(file_id, user2, 'r')
	content = user2.view_file(file_id)
	assert content == 'Hello, World!'

def test_download_file():
	user = User('test_user', 'password')
	file = File('test_file', 100, 'Hello, World!')
	file_id = user.upload_file(file)
	content = user.download_file(file_id)
	assert content == 'Hello, World!'

