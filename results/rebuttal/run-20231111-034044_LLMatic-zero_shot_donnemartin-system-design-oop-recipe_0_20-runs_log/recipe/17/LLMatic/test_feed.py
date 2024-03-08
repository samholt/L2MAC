import pytest
from feed import Feed
from follow import Follow

def test_feed():
	feed = Feed()
	follow = Follow()
	follow.follow('user1', 'user2')
	feed.add_activity('user2', 'activity1')
	assert 'activity1' in feed.get_feed('user1', follow)

	follow.unfollow('user1', 'user2')
	assert 'activity1' not in feed.get_feed('user1', follow)
