import pytest
from book_club import BookClub


def test_book_club():
	book_club = BookClub()
	assert book_club.create_club('Sci-Fi', 'A club for Sci-Fi lovers', 'public') == 'Club created successfully'
	assert book_club.create_club('Sci-Fi', 'A club for Sci-Fi lovers', 'public') == 'Club already exists'
	assert book_club.join_club('Sci-Fi', 'John') == 'User added successfully'
	assert book_club.join_club('Sci-Fi', 'John') == 'User already a member'
	assert book_club.manage_request('Sci-Fi', 'John', 'remove') == 'User removed successfully'
	assert book_club.manage_request('Sci-Fi', 'John', 'remove') == 'User not a member'
