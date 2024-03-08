import models

def test_user_model():
	user = models.User('testuser', 'testuser@test.com', 'password', ['fiction', 'non-fiction'], ['book1', 'book2'], ['book3'])
	assert user.username == 'testuser'
	assert user.email == 'testuser@test.com'
	assert user.password == 'password'
	assert user.reading_interests == ['fiction', 'non-fiction']
	assert user.read_books == ['book1', 'book2']
	assert user.wish_to_read_books == ['book3']

