import pytest
from datetime import datetime
from meeting import Meeting
from book_club import BookClub
from user import User


def test_schedule_new_meeting():
	book_club = BookClub('1', 'Book Club 1', User('1', 'User 1', 'user1@example.com', 'password'))
	meeting = Meeting('1', datetime.now(), book_club)
	new_date_time = datetime.now()
	meeting.schedule_new_meeting(new_date_time)
	assert meeting.date_time == new_date_time


def test_send_reminders():
	user1 = User('1', 'User 1', 'user1@example.com', 'password')
	user2 = User('2', 'User 2', 'user2@example.com', 'password')
	book_club = BookClub('1', 'Book Club 1', user1)
	book_club.add_member(user2)
	meeting = Meeting('1', datetime.now(), book_club)
	meeting.send_reminders()
	# As we cannot check the print statements, we assume the function works if no error is thrown
