import pytest
from book_club import BookClub

def test_book_club():
	book_club = BookClub('Book Worms', 'Public', [], ['Admin'])
	assert book_club.name == 'Book Worms'
	assert book_club.privacy_settings == 'Public'
	assert book_club.members == []
	assert book_club.administrators == ['Admin']

	book_club.create_book_club('Readers Club', 'Private', ['Admin2'])
	assert book_club.name == 'Readers Club'
	assert book_club.privacy_settings == 'Private'
	assert book_club.members == []
	assert book_club.administrators == ['Admin2']

	book_club.add_member('User1')
	assert 'User1' in book_club.members

	book_club.remove_member('User1')
	assert 'User1' not in book_club.members

	book_club.update_club_info(name='New Club', privacy_settings='Public', administrators=['Admin3'])
	assert book_club.name == 'New Club'
	assert book_club.privacy_settings == 'Public'
	assert book_club.administrators == ['Admin3']
