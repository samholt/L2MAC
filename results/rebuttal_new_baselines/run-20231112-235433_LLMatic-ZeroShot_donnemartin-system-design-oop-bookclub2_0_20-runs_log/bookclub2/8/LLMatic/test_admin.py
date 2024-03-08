import pytest
from admin import Admin


def test_admin_initialization():
	admin = Admin('admin_user', ['book_club1', 'book_club2'])
	assert admin.user == 'admin_user'
	assert admin.managed_book_clubs == ['book_club1', 'book_club2']


def test_manage_user():
	admin = Admin('admin_user', ['book_club1', 'book_club2'])
	admin.manage_user('new_user')
	# Add assertions to verify user management


def test_manage_book_club():
	admin = Admin('admin_user', ['book_club1', 'book_club2'])
	admin.manage_book_club('new_book_club')
	# Add assertions to verify book club management
