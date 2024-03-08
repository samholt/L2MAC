import pytest
import models


def test_user():
	user = models.User('username', 'email', 'password_hash')
	assert user.username == 'username'
	assert user.email == 'email'
	assert user.password_hash == 'password_hash'


def test_book_club():
	club = models.BookClub('club_name', ['user_id'])
	assert club.name == 'club_name'
	assert club.members == ['user_id']
