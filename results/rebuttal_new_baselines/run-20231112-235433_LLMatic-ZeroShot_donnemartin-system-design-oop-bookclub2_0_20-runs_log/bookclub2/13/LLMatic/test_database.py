import pytest
from database import MockDatabase
from user import User
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion
from admin import Admin

def test_mock_database():
	mock_db = MockDatabase()

	user = User('John Doe', 'password', 'johndoe@example.com')
	mock_db.add_user(user)
	assert mock_db.get_user('John Doe') == user

	book_club = BookClub('Book Club 1', 'public', [], ['John Doe'])
	mock_db.add_book_club(book_club)
	assert mock_db.get_book_club('Book Club 1') == book_club

	meeting = Meeting('2022-12-31', '12:00', ['John Doe'], [])
	mock_db.add_meeting(meeting)
	assert mock_db.get_meeting('2022-12-31') == meeting

	discussion = Discussion('Discussion 1')
	mock_db.add_discussion(discussion)
	assert mock_db.get_discussion('Discussion 1') == discussion

	admin = Admin()
	mock_db.add_admin(admin)
	assert mock_db.get_admin(admin) == admin
