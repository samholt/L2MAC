import pytest
from admin import Admin
from user import User
from book_club import BookClub


def test_admin_functions():
	admin = Admin('Admin', 'admin@example.com', 'password')
	user = User('User', 'user@example.com', 'password')
	book_club = BookClub('Book Club', 'A book club', False, admin)

	# Test manage_user_account
	admin.db.add(admin.db.users, user.email, user)
	assert user.email in admin.db.users
	admin.manage_user_account(user.email, 'delete')
	assert user.email not in admin.db.users

	# Test manage_book_club
	admin.db.add(admin.db.book_clubs, book_club.name, book_club)
	assert book_club.name in admin.db.book_clubs
	admin.manage_book_club(book_club.name, 'delete')
	assert book_club.name not in admin.db.book_clubs

	# Test remove_inappropriate_content
	admin.db.add(admin.db.discussions, '1', 'Inappropriate content')
	assert '1' in admin.db.discussions
	admin.remove_inappropriate_content('1')
	assert '1' not in admin.db.discussions

	# Test view_user_engagement
	assert admin.view_user_engagement() == (0, 0)

	# Test view_popular_books
	assert admin.view_popular_books() == []
