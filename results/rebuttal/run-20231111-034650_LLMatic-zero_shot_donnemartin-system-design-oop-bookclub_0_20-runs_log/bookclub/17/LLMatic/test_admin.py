import pytest
from admin import Admin
from database import Database
from user import User
from profile import Profile
from book_club import BookClub
from membership import Membership
from meeting import Meeting
from reminder import Reminder
from discussion import Discussion
from comment import Comment
from book import Book
from vote import Vote
from recommendation import Recommendation

def test_admin():
	admin = Admin(Database(), User(Database()), Profile(Database()), BookClub(), Membership(BookClub()), Meeting(), Reminder(), Discussion(), Comment(), Book(1, 'Test Book', 'Test Author', 'Test Description'), Vote(1, 1, 1), Recommendation(Database()))
	admin.manage_user(1, 'create', {'name': 'Test User'})
	assert admin.manage_user(1, 'get') == {'name': 'Test User'}
	admin.manage_user(1, 'update', {'name': 'Updated User'})
	assert admin.manage_user(1, 'get') == {'name': 'Updated User'}
	admin.manage_user(1, 'delete')
	assert admin.manage_user(1, 'get') is None
	admin.manage_book_club(1, 'create', 'Test Book Club')
	assert admin.manage_book_club(1, 'get') == {'club_name': 'Test Book Club', 'members': []}
	admin.manage_book_club(1, 'update', 'Updated Book Club')
	assert admin.manage_book_club(1, 'get') == {'club_name': 'Updated Book Club', 'members': []}
	admin.manage_book_club(1, 'delete')
	assert admin.manage_book_club(1, 'get') == 'Book club does not exist'
	admin.discussion.create_discussion(1, {'title': 'Test Discussion'})
	admin.remove_inappropriate_content('discussion', 1)
	assert admin.discussion.get_discussion(1) is None
	admin.comment.post_comment(1, {'content': 'Test Comment'})
	admin.remove_inappropriate_content('comment', 1)
	assert admin.comment.get_comment(1) is None
	analytics = admin.generate_analytics()
	assert analytics['user_engagement'] == 0
	assert analytics['popular_books'] == []
