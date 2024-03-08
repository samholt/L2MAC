import pytest
from book_club import BookClub
from user import User

def test_book_club():
	user1 = User('1', 'User1', 'user1@example.com', 'password1')
	user2 = User('2', 'User2', 'user2@example.com', 'password2')

	club = BookClub()
	club.create_club('1', 'Club1', user1)

	assert club.id == '1'
	assert club.name == 'Club1'
	assert club.creator == user1
	assert club.members == [user1]
	assert club.privacy == 'public'

	club.add_member(user2)
	assert club.members == [user1, user2]

	club.remove_member(user1)
	assert club.members == [user2]

	club.change_privacy('private')
	assert club.privacy == 'private'
