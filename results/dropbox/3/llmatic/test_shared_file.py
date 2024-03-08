import pytest
from user import User
from file import File
from shared_file import SharedFile


def test_shared_file():
	user = User('test_user', 'password')
	file = File('test_file', 'content', user)
	shared_file = SharedFile(file, user, [])
	user2 = User('test_user2', 'password')
	shared_file.share(user2)
	assert user2.username in shared_file.shared_with
	shared_file.unshare(user2)
	assert user2.username not in shared_file.shared_with
