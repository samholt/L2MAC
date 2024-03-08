import pytest
from book_club import BookClub
from membership import Membership


def test_membership():
	book_club = BookClub()
	membership = Membership(book_club)

	# Test joining a club
	book_club.create_book_club('1', 'Book Club 1')
	assert membership.join_club('1', 'user1') == 'User joined the club successfully'
	assert membership.join_club('1', 'user1') == 'User already a member'
	assert membership.join_club('2', 'user1') == 'Book club does not exist'

	# Test leaving a club
	assert membership.leave_club('1', 'user1') == 'User left the club successfully'
	assert membership.leave_club('1', 'user1') == 'User not a member of the club'
	assert membership.leave_club('2', 'user1') == 'Book club does not exist'
