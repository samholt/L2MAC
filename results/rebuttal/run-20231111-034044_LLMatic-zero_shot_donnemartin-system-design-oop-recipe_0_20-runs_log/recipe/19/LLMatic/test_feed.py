import pytest
from feed import Feed

def test_feed():
	feed = Feed()
	feed.add_activity('user1', 'Recipe1 created')
	feed.add_activity('user1', 'Recipe2 created')
	feed.add_activity('user2', 'Recipe3 created')
	assert feed.get_recent_activity('user1') == ['Recipe1 created', 'Recipe2 created']
	assert feed.get_recent_activity('user2') == ['Recipe3 created']
	assert feed.get_recent_activity('user3') == []
