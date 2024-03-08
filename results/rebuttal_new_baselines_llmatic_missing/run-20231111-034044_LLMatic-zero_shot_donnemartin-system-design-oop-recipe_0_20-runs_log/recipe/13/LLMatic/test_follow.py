import pytest
from follow import Follow

def test_follow():
	follow = Follow()
	follow.follow('user1', 'user2')
	assert 'user2' in follow.get_followees('user1')

	follow.follow('user1', 'user3')
	assert 'user3' in follow.get_followees('user1')

	assert 'user4' not in follow.get_followees('user1')
