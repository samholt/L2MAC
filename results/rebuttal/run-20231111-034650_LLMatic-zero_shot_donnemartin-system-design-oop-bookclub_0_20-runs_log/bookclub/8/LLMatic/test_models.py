import models

def test_user():
	user = models.User('testuser', 'testuser@example.com', 'password')
	assert user.username == 'testuser'
	assert user.email == 'testuser@example.com'
	assert user.password == 'password'
	assert user.read_books == []
	assert user.wish_list == []
	assert user.followed_users == []

def test_book_club():
	admin = models.User('admin', 'admin@example.com', 'password')
	book_club = models.BookClub('Test Book Club', 'This is a test book club.', True, admin)
	assert book_club.name == 'Test Book Club'
	assert book_club.description == 'This is a test book club.'
	assert book_club.is_private == True
	assert book_club.members == []
	assert book_club.admin == admin
	assert book_club.meetings == []
	assert book_club.discussions == []
