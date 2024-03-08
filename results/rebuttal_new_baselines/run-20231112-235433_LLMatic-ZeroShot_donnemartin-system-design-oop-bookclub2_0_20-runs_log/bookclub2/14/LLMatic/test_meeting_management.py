import pytest
import app

# Test scheduling a meeting
def test_schedule_meeting():
	app.DATABASE['book_clubs']['Test Club'] = app.BookClub('Test Club', 'public', app.User('admin', 'password', 'admin@test.com'))
	response = app.app.test_client().post('/schedule_meeting', json={'date': '2022-12-31', 'time': '12:00', 'book_club': 'Test Club'})
	assert response.data == b'Meeting scheduled successfully!'
	assert isinstance(app.DATABASE['meetings']['2022-12-31'], app.Meeting)

# Test scheduling a meeting with invalid book club
def test_schedule_meeting_invalid_book_club():
	response = app.app.test_client().post('/schedule_meeting', json={'date': '2022-12-31', 'time': '12:00', 'book_club': 'Invalid Club'})
	assert response.data == b'Invalid book club'
