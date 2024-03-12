import pytest
from user import User

def test_create_account():
	user = User('testuser', 'testpassword')
	user.create_account()
	assert user.username == 'testuser'
	assert user.password == 'testpassword'


def test_view_urls():
	user = User('testuser', 'testpassword')
	user.urls = {'google.com': 'ggl'}
	assert user.view_urls() == {'google.com': 'ggl'}


def test_edit_url():
	user = User('testuser', 'testpassword')
	user.urls = {'google.com': 'ggl'}
	user.edit_url('google.com', 'yahoo.com')
	assert user.view_urls() == {'yahoo.com': 'ggl'}


def test_delete_url():
	user = User('testuser', 'testpassword')
	user.urls = {'google.com': 'ggl'}
	user.delete_url('google.com')
	assert user.view_urls() == {}
