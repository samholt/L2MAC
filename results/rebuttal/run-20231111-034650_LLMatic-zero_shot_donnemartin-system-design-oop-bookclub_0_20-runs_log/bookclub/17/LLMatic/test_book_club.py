import pytest
from book_club import BookClub


def test_book_club():
	book_club = BookClub()

	# Test creating a book club
	assert book_club.create_book_club('1', 'Book Club 1') == 'Book club created successfully'
	assert book_club.create_book_club('1', 'Book Club 1') == 'Book club already exists'

	# Test retrieving a book club
	assert book_club.get_book_club('1') == {'club_name': 'Book Club 1', 'members': []}
	assert book_club.get_book_club('2') == 'Book club does not exist'

	# Test updating a book club
	assert book_club.update_book_club('1', 'Book Club 1 Updated') == 'Book club updated successfully'
	assert book_club.get_book_club('1') == {'club_name': 'Book Club 1 Updated', 'members': []}
	assert book_club.update_book_club('2', 'Book Club 2') == 'Book club does not exist'

	# Test deleting a book club
	assert book_club.delete_book_club('1') == 'Book club deleted successfully'
	assert book_club.get_book_club('1') == 'Book club does not exist'
