import pytest
from follow import Follow

def test_follow():
	follow = Follow()
	follow.follow('user1', 'user2')
	assert 'user2' in follow.get_followees('user1')

	follow.unfollow('user1', 'user2')
	assert 'user2' not in follow.get_followees('user1')
