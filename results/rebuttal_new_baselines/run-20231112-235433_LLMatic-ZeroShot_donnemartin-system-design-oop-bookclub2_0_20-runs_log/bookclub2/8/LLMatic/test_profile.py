import pytest
from profile import Profile


def test_follow():
	user1 = 'Alice'
	user2 = 'Bob'
	profile1 = Profile(user1)
	profile2 = Profile(user2)
	profile1.follow(user2)
	assert user2 in profile1.followers


def test_add_book():
	user = 'Alice'
	book = 'Moby Dick'
	profile = Profile(user)
	profile.add_book(book)
	assert book in profile.books_read
