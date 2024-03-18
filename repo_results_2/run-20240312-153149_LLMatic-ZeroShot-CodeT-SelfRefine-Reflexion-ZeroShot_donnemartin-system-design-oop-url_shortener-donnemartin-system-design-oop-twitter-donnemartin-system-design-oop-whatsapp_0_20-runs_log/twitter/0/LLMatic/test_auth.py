import pytest
from auth import app
from user import User


def test_follow():
	User.users.clear()
	User(1, 'test1@test.com', 'test1', 'password')
	User(2, 'test2@test.com', 'test2', 'password')
	User.users[1].follow(2)
	assert 2 in User.users[1].following


def test_unfollow():
	User.users.clear()
	User(1, 'test1@test.com', 'test1', 'password')
	User(2, 'test2@test.com', 'test2', 'password')
	User.users[1].follow(2)
	User.users[1].unfollow(2)
	assert 2 not in User.users[1].following

