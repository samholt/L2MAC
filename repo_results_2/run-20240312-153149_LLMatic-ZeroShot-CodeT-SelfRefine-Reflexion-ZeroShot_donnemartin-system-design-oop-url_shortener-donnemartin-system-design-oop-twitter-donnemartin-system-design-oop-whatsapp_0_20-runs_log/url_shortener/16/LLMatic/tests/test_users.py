import pytest
from services import create_user, get_user, edit_user, delete_user


def test_create_user():
	user = create_user('testuser', 'testpassword')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'
	assert user.urls == []


def test_get_user():
	user = get_user('testuser')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'
	assert user.urls == []


def test_edit_user():
	user = edit_user('testuser', 'newpassword')
	assert user.username == 'testuser'
	assert user.password == 'newpassword'
	assert user.urls == []


def test_delete_user():
	message = delete_user('testuser')
	assert message == 'User deleted'
	user = get_user('testuser')
	assert user is None
