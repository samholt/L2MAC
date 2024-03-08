import pytest
from admin import Admin


def test_admin():
	admin = Admin()

	# Test user creation
	admin.create_user('Alice')
	assert 'Alice' in admin.users

	# Test user deletion
	admin.delete_user('Alice')
	assert 'Alice' not in admin.users

	# Test book club creation
	admin.create_book_club()
	assert admin.book_clubs is not None

	# Test meeting creation
	admin.create_meeting()
	assert admin.meetings is not None

	# Test discussion creation
	admin.create_discussion()
	assert admin.discussions is not None

	# Test analytics generation
	analytics = admin.generate_analytics()
	assert analytics == {'users': 0, 'book_clubs': 0, 'meetings': 0, 'discussions': 0}
