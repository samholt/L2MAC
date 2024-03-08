import pytest
from community import Community

def test_follow():
	community = Community()
	community.follow('user1', 'user2')
	assert 'user2' in community.following['user1']

def test_generate_feed():
	community = Community()
	community.follow('user1', 'user2')
	community.feed['user2'] = ['recipe1']
	community.generate_feed('user1')
	assert 'recipe1' in community.feed['user1']

def test_share_recipe():
	community = Community()
	result = community.share_recipe('user1', 'recipe1', 'Facebook')
	assert result == 'User user1 shared recipe recipe1 on Facebook'
