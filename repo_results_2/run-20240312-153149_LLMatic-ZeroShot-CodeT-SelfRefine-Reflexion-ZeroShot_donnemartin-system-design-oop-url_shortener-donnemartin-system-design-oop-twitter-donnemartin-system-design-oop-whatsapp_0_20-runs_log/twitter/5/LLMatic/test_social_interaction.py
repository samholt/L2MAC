from social_interaction import SocialInteraction
import pytest


def test_follow_unfollow():
	interaction = SocialInteraction()
	interaction.follow('user1', 'user2')
	assert 'user2' in interaction.following['user1']
	assert 'user1' in interaction.followers['user2']
	interaction.unfollow('user1', 'user2')
	assert 'user2' not in interaction.following['user1']
	assert 'user1' not in interaction.followers['user2']


def test_timeline():
	interaction = SocialInteraction()
	interaction.follow('user1', 'user2')
	interaction.notify_followers('user2', {'content': 'Hello, world!', 'timestamp': 1234567890})
	timeline = interaction.get_timeline('user1')
	assert len(timeline) == 1
	assert timeline[0]['content'] == 'Hello, world!'


def test_notify_followers():
	interaction = SocialInteraction()
	interaction.follow('user1', 'user2')
	interaction.notify_followers('user2', {'content': 'Hello, world!', 'timestamp': 1234567890})
	assert len(interaction.posts['user2']) == 1
	assert interaction.posts['user2'][0]['content'] == 'Hello, world!'


def test_conversation():
	interaction = SocialInteraction()
	interaction.create_conversation('user1', 'user2')
	interaction.send_message('user1', 'user2', {'content': 'Hello, user2!', 'timestamp': 1234567890})
	conversation = interaction.get_conversation('user1', 'user2')
	assert len(conversation) == 1
	assert conversation[0]['content'] == 'Hello, user2!'


def test_block_unblock():
	interaction = SocialInteraction()
	interaction.block_user('user1', 'user2')
	assert interaction.is_blocked('user1', 'user2')
	interaction.unblock_user('user1', 'user2')
	assert not interaction.is_blocked('user1', 'user2')


def test_notifications():
	interaction = SocialInteraction()
	interaction.like('user1', {'user': 'user2', 'content': 'Hello, world!', 'timestamp': 1234567890})
	interaction.retweet('user1', {'user': 'user2', 'content': 'Hello, world!', 'timestamp': 1234567890})
	interaction.reply('user1', {'user': 'user2', 'content': 'Hello, world!', 'timestamp': 1234567890}, 'Nice post!')
	interaction.mention('user1', {'user': 'user2', 'content': 'Hello, @user3!', 'timestamp': 1234567890}, 'user3')
	assert len(interaction.notifications['user2']) == 3
	assert len(interaction.notifications['user3']) == 1
