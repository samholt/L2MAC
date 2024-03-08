import pytest
from book_club import BookClub

def test_create_club():
	club = BookClub('My Book Club', 'Public', [], ['Admin'])
	assert club.name == 'My Book Club'
	assert club.privacy_settings == 'Public'
	assert club.members == []
	assert club.administrators == ['Admin']


def test_add_member():
	club = BookClub('My Book Club', 'Public', [], ['Admin'])
	club.add_member('User1')
	assert 'User1' in club.members


def test_remove_member():
	club = BookClub('My Book Club', 'Public', ['User1'], ['Admin'])
	club.remove_member('User1')
	assert 'User1' not in club.members


def test_update_privacy_settings():
	club = BookClub('My Book Club', 'Public', [], ['Admin'])
	club.update_privacy_settings('Private')
	assert club.privacy_settings == 'Private'
