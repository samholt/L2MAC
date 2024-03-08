import models


def test_user():
	user = models.User('testuser', 'testuser@test.com', 'testpassword')
	assert user.username == 'testuser'
	assert user.email == 'testuser@test.com'
	assert user.password == 'testpassword'
	assert user.books_read == []


def test_bookclub():
	book_club = models.BookClub('testclub', 'This is a test club', False)
	assert book_club.name == 'testclub'
	assert book_club.description == 'This is a test club'
	assert book_club.is_private == False
	assert book_club.members == []
	assert book_club.current_book == None
	assert book_club.meetings == []


def test_meeting():
	book_club = models.BookClub('testclub', 'This is a test club', False)
	meeting = models.Meeting('2022-01-01', '10:00', ['testuser'], book_club)
	assert meeting.date == '2022-01-01'
	assert meeting.time == '10:00'
	assert meeting.attendees == ['testuser']
	assert meeting.book_club == book_club
	assert meeting.to_ical() == 'BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\nDTSTART:20220101T100000\nSUMMARY:Meeting of testclub\nEND:VEVENT\nEND:VCALENDAR'
