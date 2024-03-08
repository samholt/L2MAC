import pytest
from feed import Feed

def test_feed():
	feed = Feed()
	feed.add_activity('user1', 'activity1')
	assert 'activity1' in feed.get_feed('user1')

	feed.add_activity('user1', 'activity2')
	assert 'activity2' in feed.get_feed('user1')

	assert 'activity3' not in feed.get_feed('user1')
