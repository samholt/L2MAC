import pytest
from book_club import BookClub

def test_book_club():
	book_club = BookClub()

	# Test club creation
	assert book_club.create_club('Club1', False) == 'Club created successfully'
	assert book_club.create_club('Club1', False) == 'Club already exists'

	# Test setting club privacy
	assert book_club.set_privacy('Club1', True) == 'Club privacy updated successfully'
	assert book_club.set_privacy('Club2', True) == 'Club does not exist'

	# Test joining club
	assert book_club.join_club('Club1', 'User1') == 'Cannot join private club'
	assert book_club.join_club('Club2', 'User1') == 'Club does not exist'
	book_club.set_privacy('Club1', False)
	assert book_club.join_club('Club1', 'User1') == 'Joined club successfully'

	# Test managing members
	assert book_club.manage_member('Club1', 'User2', 'add') == 'Member managed successfully'
	assert book_club.manage_member('Club1', 'User1', 'remove') == 'Member managed successfully'
	assert book_club.manage_member('Club2', 'User1', 'add') == 'Club does not exist'
