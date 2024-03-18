import pytest
from user_accounts import User, users

@pytest.fixture
def user():
	User.register('test', 'password')
	User.add_url('test', 'short', 'long')
	User.register('test2', 'password2')
	User.add_url('test2', 'short2', 'long2')
	User.register('test3', 'password3')
	User.add_url('test3', 'short3', 'long3')
	User.register('test4', 'password4')
	User.add_url('test4', 'short4', 'long4')
	return users['test']

def test_register(user):
	assert User.register('test5', 'password') == True
	assert User.register('test', 'password') == False

def test_login(user):
	assert User.login('test', 'password') == True
	assert User.login('test', 'wrong_password') == False

def test_add_url(user):
	assert User.add_url('test', 'short5', 'long5') == True
	assert User.add_url('test5', 'short5', 'long5') == True

def test_view_urls(user):
	assert User.view_urls('test') == {'short': 'long', 'short5': 'long5'}

def test_edit_url(user):
	assert User.edit_url('test', 'short', 'long5') == True
	assert User.edit_url('test5', 'short5', 'long5') == True

def test_delete_url(user):
	assert User.delete_url('test', 'short') == True
	assert User.delete_url('test5', 'short5') == True

def test_view_all_urls(user):
	assert User.view_all_urls() == {'test': {'short': 'long', 'short5': 'long5'}, 'test2': {'short2': 'long2'}, 'test3': {'short3': 'long3'}, 'test4': {'short4': 'long4'}, 'test5': {}}

def test_delete_user(user):
	assert User.delete_user('test') == True
	assert User.delete_user('test5') == True

