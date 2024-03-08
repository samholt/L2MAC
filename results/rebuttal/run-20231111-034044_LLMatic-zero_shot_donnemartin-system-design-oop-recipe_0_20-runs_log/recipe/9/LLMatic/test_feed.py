import pytest
from feed import Feed
from user import User


def test_feed():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user3 = User('user3', 'password3')

	# User1 follows user2 and user3
	user1.follow_user(user2)
	user1.follow_user(user3)

	# User2 and user3 have some activity
	user2.add_activity({'type': 'recipe', 'date': '2021-12-01', 'content': 'Recipe 1'})
	user3.add_activity({'type': 'review', 'date': '2021-12-02', 'content': 'Review 1'})

	# Generate feed for user1
	feed = Feed(user1)
	feed_items = feed.generate_feed()

	# Check that the feed items are in the correct order
	assert feed_items[0]['date'] == '2021-12-02'
	assert feed_items[1]['date'] == '2021-12-01'
