import pytest
from sharing import Sharing
from user import User
from file import File

def test_sharing():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	shared_by = User('test_user1', 'test_password1')
	shared_with = User('test_user2', 'test_password2')
	sharing = Sharing(file, shared_by, shared_with)
	sharing.share()
	assert sharing.file == file
	assert sharing.shared_by == shared_by
	assert sharing.shared_with == shared_with

def test_unshare():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	shared_by = User('test_user1', 'test_password1')
	shared_with = User('test_user2', 'test_password2')
	sharing = Sharing(file, shared_by, shared_with)
	sharing.unshare()
	# Add assertions for unshare

def test_get_shared_files():
	file = File('test_file', 1024, 'txt', 'This is a test file')
	shared_by = User('test_user1', 'test_password1')
	shared_with = User('test_user2', 'test_password2')
	sharing = Sharing(file, shared_by, shared_with)
	shared_files = sharing.get_shared_files()
	# Add assertions for get_shared_files
