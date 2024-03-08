import pytest
from admin import Admin
from user import User, users
from book_club import BookClub
from discussion import Discussion

admin = Admin()
user = User('test_user', ['fiction'])
users[user.name] = user
admin.users[user.name] = user
book_club = BookClub()
book_club.create_club('test_club', 'A club for testing', 'public')
admin.book_clubs['test_club'] = book_club
discussion = Discussion()
discussion.create_discussion('test_topic', 'test_club')
admin.discussions['test_topic'] = discussion

def test_manage_user():
	assert admin.manage_user('test_user', 'remove') == 'User removed successfully'
	assert admin.manage_user('non_existent_user', 'remove') == 'User not found'

	user = User('test_user', ['fiction'])
	users[user.name] = user
	admin.users[user.name] = user
	assert admin.manage_user('test_user', 'suspend') == 'User suspended successfully'
	assert admin.manage_user('non_existent_user', 'suspend') == 'User not found'

	assert users['test_user'].active == False

def test_manage_book_club():
	assert admin.manage_book_club('test_club', 'remove') == 'Book club removed successfully'
	assert admin.manage_book_club('non_existent_club', 'remove') == 'Book club not found'

	book_club = BookClub()
	book_club.create_club('test_club', 'A club for testing', 'public')
	admin.book_clubs['test_club'] = book_club

def test_remove_content():
	assert admin.remove_content('test_topic') == 'Discussion removed successfully'
	assert admin.remove_content('non_existent_topic') == 'Discussion not found'

	discussion = Discussion()
	discussion.create_discussion('test_topic', 'test_club')
	admin.discussions['test_topic'] = discussion

def test_generate_analytics():
	analytics = admin.generate_analytics()
	assert analytics['user_engagement']['test_user'] == 0
	assert analytics['popular_books']['test_club'] == 0
