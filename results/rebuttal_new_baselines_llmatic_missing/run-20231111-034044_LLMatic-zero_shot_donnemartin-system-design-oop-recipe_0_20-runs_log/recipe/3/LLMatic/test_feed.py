import pytest
from user import User
from feed import Feed


def test_feed():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user3 = User('user3', 'password3')
	
	# User1 follows User2 and User3
	user1.follow_user(user2)
	user1.follow_user(user3)
	
	# User2 and User3 have some activity
	user2.add_activity({'action': 'posted', 'timestamp': '2022-01-01T00:00:00Z'})
	user3.add_activity({'action': 'liked', 'timestamp': '2022-01-02T00:00:00Z'})
	
	feed = Feed(user1)
	
	# Check the feed of User1
	assert feed.show_recent_activity() == [
		{'action': 'liked', 'timestamp': '2022-01-02T00:00:00Z'},
		{'action': 'posted', 'timestamp': '2022-01-01T00:00:00Z'}
	]
