import pytest
from book_club import BookClub
from user import User

def test_book_club_creation():
	book_club = BookClub('Sci-fi Lovers', 'A club for all sci-fi book lovers', False)
	assert book_club.name == 'Sci-fi Lovers'
	assert book_club.description == 'A club for all sci-fi book lovers'
	assert book_club.is_private == False
	assert book_club.members == []
	assert book_club.books == []

def test_add_member():
	book_club = BookClub('Sci-fi Lovers', 'A club for all sci-fi book lovers', False)
	user = User('john_doe', 'password123', 'john_doe@example.com')
	book_club.add_member(user)
	assert user in book_club.members

def test_add_book():
	book_club = BookClub('Sci-fi Lovers', 'A club for all sci-fi book lovers', False)
	book = 'Dune'
	book_club.add_book(book)
	assert book in book_club.books
