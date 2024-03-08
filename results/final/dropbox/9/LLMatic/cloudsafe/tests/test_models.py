import pytest
from cloudsafe.app.models import User, File
from cloudsafe.app import db


def test_user_model():
	user = User('Test User', 'test@example.com')
	assert user.username == 'Test User'
	assert user.email == 'test@example.com'


def test_file_model():
	user = User('Test User', 'test@example.com')
	file = File('test.txt', b'test data', user)
	assert file.filename == 'test.txt'
	assert file.data == b'test data'
	assert file.owner == user
