import pytest
from status import Status


def test_post():
	status = Status('User1', 'Hello, world!')
	assert 'User1 posted: Hello, world!' in status.post()


def test_view():
	status = Status('User1', 'Hello, world!')
	assert 'Hello, world!' == status.view('User2')

	status.set_visibility('private')
	assert 'This status is private.' == status.view('User2')

	status.add_viewer('User2')
	assert 'Hello, world!' == status.view('User2')


def test_set_visibility():
	status = Status('User1', 'Hello, world!')
	status.set_visibility('private')
	assert 'private' == status.visibility


def test_add_viewer():
	status = Status('User1', 'Hello, world!')
	status.add_viewer('User2')
	assert 'User2' in status.viewers
