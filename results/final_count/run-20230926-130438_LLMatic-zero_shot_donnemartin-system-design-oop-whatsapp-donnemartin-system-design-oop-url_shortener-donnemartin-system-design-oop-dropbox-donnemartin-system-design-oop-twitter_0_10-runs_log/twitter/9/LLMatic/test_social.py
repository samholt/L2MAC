import pytest
from social import Social

def test_follow():
	social = Social()
	social.follow('user1', 'user2')
	assert 'user2' in social.following['user1']
	assert 'user1' in social.followers['user2']

def test_unfollow():
	social = Social()
	social.follow('user1', 'user2')
	social.unfollow('user1', 'user2')
	assert 'user2' not in social.following['user1']
	assert 'user1' not in social.followers['user2']

def test_notify():
	social = Social()
	social.follow('user1', 'user2')
	assert 'user1' in social.notify('user2')

def test_view_timeline():
	social = Social()
	social.follow('user1', 'user2')
	assert 'user2' in social.view_timeline('user1')

def test_send_message():
	social = Social()
	social.send_message('user1', 'user2', 'Hello')
	assert 'Hello' in social.view_messages('user1', 'user2')

def test_block_user():
	social = Social()
	social.block_user('user1', 'user2')
	assert 'user2' in social.blocked['user1']

def test_unblock_user():
	social = Social()
	social.block_user('user1', 'user2')
	social.unblock_user('user1', 'user2')
	assert 'user2' not in social.blocked['user1']

def test_notify_like():
	social = Social()
	social.notify_like('user1', 'user2')
	assert 'user1 liked your post' in social.view_notifications('user2')

def test_notify_retweet():
	social = Social()
	social.notify_retweet('user1', 'user2')
	assert 'user1 retweeted your post' in social.view_notifications('user2')

def test_notify_reply():
	social = Social()
	social.notify_reply('user1', 'user2')
	assert 'user1 replied to your post' in social.view_notifications('user2')

def test_notify_mention():
	social = Social()
	social.notify_mention('user1', 'user2')
	assert 'user1 mentioned you in a post' in social.view_notifications('user2')
