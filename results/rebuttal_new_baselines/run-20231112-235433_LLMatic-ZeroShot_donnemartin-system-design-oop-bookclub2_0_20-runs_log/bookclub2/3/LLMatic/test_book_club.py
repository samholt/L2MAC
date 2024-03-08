import pytest
import book_club


def test_create_club_missing_data():
	with pytest.raises(ValueError):
		book_club.BookClub('', '')


def test_join_club_missing_data():
	club = book_club.BookClub('Test Club')
	with pytest.raises(ValueError):
		club.join_club('')


def test_set_privacy_missing_data():
	club = book_club.BookClub('Test Club')
	with pytest.raises(ValueError):
		club.set_privacy('')


def test_manage_roles_missing_data():
	club = book_club.BookClub('Test Club')
	with pytest.raises(ValueError):
		club.manage_roles('', '', '')
