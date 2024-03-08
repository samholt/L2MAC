import pytest
from user import User

def test_create_user():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'
	assert user.email == 'testemail@test.com'
	assert user.book_clubs == []

def test_authenticate():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	assert user.authenticate('testuser', 'testpassword') == True
	assert user.authenticate('wronguser', 'wrongpassword') == False

def test_join_book_club():
	user = User('testuser', 'testpassword', 'testemail@test.com')
	user.join_book_club('bookclub1')
	assert 'bookclub1' in user.book_clubs
