import pytest
from user import User


def test_user_registration():
	user = User()
	assert user.register('test', 'password')
	assert not user.register('test', 'password')


def test_user_authentication():
	user = User()
	user.register('test', 'password')
	assert user.authenticate('test', 'password')
	assert not user.authenticate('test', 'wrong_password')
	assert not user.authenticate('wrong_user', 'password')


def test_add_url():
	user = User()
	user.register('test', 'password')
	assert user.add_url('test', 'short', 'original')
	assert not user.add_url('wrong_user', 'short', 'original')


def test_get_urls():
	user = User()
	user.register('test', 'password')
	user.add_url('test', 'short', 'original')
	assert user.get_urls('test') == {'short': 'original'}
	assert user.get_urls('wrong_user') == {}


def test_edit_url():
	user = User()
	user.register('test', 'password')
	user.add_url('test', 'short', 'original')
	assert user.edit_url('test', 'short', 'new')
	assert not user.edit_url('test', 'wrong_short', 'new')
	assert not user.edit_url('wrong_user', 'short', 'new')
	assert user.get_urls('test') == {'short': 'new'}


def test_delete_url():
	user = User()
	user.register('test', 'password')
	user.add_url('test', 'short', 'original')
	assert user.delete_url('test', 'short')
	assert not user.delete_url('test', 'wrong_short')
	assert not user.delete_url('wrong_user', 'short')
	assert user.get_urls('test') == {}
