import models

def test_user():
	user = models.User('testuser', 'testuser@test.com', 'passwordhash')
	assert user.username == 'testuser'
	assert user.email == 'testuser@test.com'
	assert user.password_hash == 'passwordhash'


def test_book_club():
	book_club = models.BookClub('testclub', 'This is a test club')
	assert book_club.name == 'testclub'
	assert book_club.description == 'This is a test club'
	assert book_club.privacy == 'public'
	book_club.set_privacy('private')
	assert book_club.privacy == 'private'
