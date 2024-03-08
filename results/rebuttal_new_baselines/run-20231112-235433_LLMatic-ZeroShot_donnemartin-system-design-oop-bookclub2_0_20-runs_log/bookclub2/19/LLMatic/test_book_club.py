import pytest
from book_club import BookClub

def test_create_club():
	club = BookClub(None, None, None)
	club.create_club('1', 'Book Lovers', 'Public')
	assert club.club_id == '1'
	assert club.name == 'Book Lovers'
	assert club.privacy == 'Public'
	assert club.members == []

def test_add_member():
	club = BookClub('1', 'Book Lovers', 'Public')
	club.add_member('John')
	assert 'John' in club.members

def test_update_club_info():
	club = BookClub('1', 'Book Lovers', 'Public')
	club.update_club_info(name='Book Worms', privacy='Private')
	assert club.name == 'Book Worms'
	assert club.privacy == 'Private'
