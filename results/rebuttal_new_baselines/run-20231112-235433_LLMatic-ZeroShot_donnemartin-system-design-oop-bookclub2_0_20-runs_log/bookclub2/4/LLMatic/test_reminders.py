import app
import models
import time
import io
import sys
import threading

def test_reminders():
	# Capture the output of the application
	captured_output = io.StringIO()
	sys.stdout = captured_output

	# Create a user and a book club
	user = models.User('testuser', 'testuser@example.com', 'password')
	app.users['testuser'] = user
	bookclub = models.BookClub('testclub', 'public', user)
	app.bookclubs['testclub'] = bookclub

	# Add a meeting to the book club
	meeting = models.Meeting('2022-12-31', '12:00', 'Test Location')
	bookclub.add_meeting(meeting)

	# Manually send a reminder for the meeting
	meeting.send_reminder()

	# Check if a reminder was sent for the meeting
	assert meeting.is_reminder_sent()

	# Reset the standard output
	sys.stdout = sys.__stdout__

	# Start the reminder thread
	threading.Thread(target=app.send_reminders).start()

	# Wait for the reminder thread to run
	time.sleep(1)

	# Check the output of the application
	assert 'Sending reminder for meeting on 2022-12-31 at 12:00 in Test Location to all members of testclub' in captured_output.getvalue()

	# Reset the standard output
	sys.stdout = sys.__stdout__
