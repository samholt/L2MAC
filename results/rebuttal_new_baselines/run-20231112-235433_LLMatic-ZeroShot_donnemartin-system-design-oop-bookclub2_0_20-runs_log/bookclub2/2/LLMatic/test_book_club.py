import pytest
from book_club import BookClub
from user import User

def test_book_club():
	club = BookClub('1', 'Book Lovers', 'Public')
	user1 = User('1', 'John Doe', 'john.doe@example.com', 'password')
	user2 = User('2', 'Jane Doe', 'jane.doe@example.com', 'password')

	club.add_member(user1)
	club.add_member(user2)

	assert club.get_club_info() == {'id': '1', 'name': 'Book Lovers', 'privacy_settings': 'Public', 'members': [{'id': '1', 'name': 'John Doe', 'email': 'john.doe@example.com'}, {'id': '2', 'name': 'Jane Doe', 'email': 'jane.doe@example.com'}]}

	club.remove_member(user1)

	assert club.get_club_info() == {'id': '1', 'name': 'Book Lovers', 'privacy_settings': 'Public', 'members': [{'id': '2', 'name': 'Jane Doe', 'email': 'jane.doe@example.com'}]}
