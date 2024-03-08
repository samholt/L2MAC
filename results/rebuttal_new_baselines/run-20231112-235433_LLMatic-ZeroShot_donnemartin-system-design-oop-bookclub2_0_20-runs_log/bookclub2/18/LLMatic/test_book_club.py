import pytest
from book_club import BookClub
from user import User

def test_book_club():
	book_club = BookClub('Sci-Fi Lovers', 'Public')
	assert book_club.name == 'Sci-Fi Lovers'
	assert book_club.privacy_setting == 'Public'
	assert book_club.members == []
	assert book_club.books == []

	user = User('testuser', 'password', 'testuser@example.com')
	book_club.add_member(user)
	assert book_club.members == [user]

	book_club.add_book('Dune')
	assert book_club.books == ['Dune']
