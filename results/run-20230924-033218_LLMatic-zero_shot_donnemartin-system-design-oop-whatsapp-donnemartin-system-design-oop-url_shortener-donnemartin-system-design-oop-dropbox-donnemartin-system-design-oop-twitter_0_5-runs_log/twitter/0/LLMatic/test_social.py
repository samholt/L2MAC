import pytest
from auth import register, follow_user, unfollow_user, block_user, unblock_user
from social import send_message, get_conversation


def test_follow_unfollow_block_unblock():
	user1 = register('user1', 'user1@example.com', 'password1')
	user2 = register('user2', 'user2@example.com', 'password2')
	assert user1.following == []
	assert user2.followers == []
	follow_user('user1', 'user2')
	assert user2 in user1.following
	assert user1 in user2.followers
	unfollow_user('user1', 'user2')
	assert user2 not in user1.following
	assert user1 not in user2.followers
	block_user('user1', 'user2')
	assert user2 in user1.blocked
	unblock_user('user1', 'user2')
	assert user2 not in user1.blocked


def test_send_message_get_conversation():
	user1 = register('user1', 'user1@example.com', 'password1')
	user2 = register('user2', 'user2@example.com', 'password2')
	message1 = send_message(user1.id, user2.id, 'Hello, user2!')
	message2 = send_message(user2.id, user1.id, 'Hello, user1!')
	conversation = get_conversation(user1.id, user2.id)
	assert conversation == [message1, message2]

