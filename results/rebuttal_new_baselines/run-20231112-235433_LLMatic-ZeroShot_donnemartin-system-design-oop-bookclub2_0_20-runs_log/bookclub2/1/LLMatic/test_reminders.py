import unittest
from unittest.mock import patch
from models import User, BookClub, Meeting

class TestReminders(unittest.TestCase):
	@patch('builtins.print')
	@patch('app.book_clubs')
	def test_send_reminders(self, mock_book_clubs, mock_print):
		# Arrange
		user = User('testuser', 'testuser@example.com', 'password_hash')
		meeting = Meeting('2022-12-31', '12:00')
		book_club = BookClub('testclub', 'A book club for testing')
		book_club.add_member(user)
		book_club.schedule_meeting(meeting)
		mock_book_clubs.values.return_value = [book_club]
		
		# Act
		from app import send_reminders
		send_reminders()
		
		# Assert
		mock_print.assert_called_with('Sending reminder to testuser@example.com about meeting on 2022-12-31 at 12:00')

if __name__ == '__main__':
	unittest.main()
