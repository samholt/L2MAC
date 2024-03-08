import pytest
from admin import Admin


def test_manage_book_club():
	admin = Admin()
	admin.manage_book_club('book_club_1', 'delete')
	assert 'book_club_1' not in admin.admin_data


def test_manage_user_account():
	admin = Admin()
	admin.manage_user_account('user_1', 'delete')
	assert 'user_1' not in admin.admin_data


def test_remove_content():
	admin = Admin()
	admin.remove_content('content_1')
	assert 'content_1' not in admin.admin_data


def test_view_analytics():
	admin = Admin()
	admin.admin_data = {'book_club_1': 'data'}
	assert admin.view_analytics() == {'book_club_1': 'data'}
