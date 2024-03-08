import pytest
from book_club import BookClub


def test_book_club():
	club = BookClub('Sci-Fi Lovers', 'A club for science fiction enthusiasts', False, 'admin1')
	assert club.name == 'Sci-Fi Lovers'
	assert club.description == 'A club for science fiction enthusiasts'
	assert club.is_private == False
	assert club.members == ['admin1']
	assert club.admins == ['admin1']

	club.create_club('Fantasy Fans', 'A club for fantasy book lovers', True, 'admin2')
	assert club.name == 'Fantasy Fans'
	assert club.description == 'A club for fantasy book lovers'
	assert club.is_private == True
	assert club.members == ['admin2']
	assert club.admins == ['admin2']

	club.update_club_info(name='Mystery Maniacs', description='A club for mystery book lovers')
	assert club.name == 'Mystery Maniacs'
	assert club.description == 'A club for mystery book lovers'

	club.add_member('user1')
	assert 'user1' in club.members

	club.remove_member('user1')
	assert 'user1' not in club.members

	club.manage_member_requests('user2', 'approve')
	assert 'user2' in club.members

	club.manage_member_requests('user2', 'deny')
	assert 'user2' not in club.members

	club.manage_permissions('admin2', 'demote')
	assert 'admin2' not in club.admins

	club.manage_permissions('user2', 'promote')
	assert 'user2' not in club.admins
