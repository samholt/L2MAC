import pytest
from user import User, users

def test_create_user():
	user = User('Alice', ['Fantasy', 'Sci-Fi'])
	users[user.name] = user
	assert user.name == 'Alice'
	assert user.interests == ['Fantasy', 'Sci-Fi']
	assert user.book_lists == {}
	assert user.following == []

def test_follow_user():
	user1 = User('Alice', ['Fantasy', 'Sci-Fi'])
	user2 = User('Bob', ['Mystery', 'Thriller'])
	users[user1.name] = user1
	users[user2.name] = user2
	user1.follow_user(user2)
	assert user2 in user1.following
