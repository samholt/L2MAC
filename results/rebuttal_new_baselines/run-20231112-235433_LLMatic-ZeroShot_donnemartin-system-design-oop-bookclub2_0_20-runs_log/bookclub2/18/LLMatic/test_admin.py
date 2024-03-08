import pytest
from admin import Admin

def test_moderate_content():
	admin = Admin({'id': 1, 'name': 'Admin'})
	content = {'id': 1, 'text': 'Test content'}
	assert admin.moderate_content(content) == 'Content with id 1 is moderated'

def test_manage_users():
	admin = Admin({'id': 1, 'name': 'Admin'})
	user = {'id': 1, 'name': 'User'}
	assert admin.manage_users(user) == 'User with id 1 is managed'
