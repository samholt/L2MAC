import pytest
from community import Community

def test_follow():
	community = Community()
	community.follow('user1', 'user2')
	assert 'user2' in community.generate_feed('user1')

def test_share_recipe():
	community = Community()
	message = community.share_recipe('user1', 'recipe1', 'Facebook')
	assert message == 'User user1 shared recipe recipe1 on Facebook'
