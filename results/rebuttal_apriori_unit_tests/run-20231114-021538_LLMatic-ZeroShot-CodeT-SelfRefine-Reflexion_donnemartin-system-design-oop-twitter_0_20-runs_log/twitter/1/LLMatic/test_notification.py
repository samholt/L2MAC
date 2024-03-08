import pytest
from notification import get_notifications
from user import register_user, follow_user
from post import create_post
from message import send_message

def test_get_notifications():
	# Register two users
	register_user('user1', 'user1@example.com', 'password1')
	register_user('user2', 'user2@example.com', 'password2')
	# User1 follows User2
	follow_user('user1@example.com', 2)
	# User2 creates a post
	create_post(2, 'Hello, world!')
	# User2 sends a message to User1
	send_message(2, 1, 'Hello, User1!')
	# Get User1's notifications
	posts, messages = get_notifications('user1@example.com')
	# Check that User1 has one post and one message in their notifications
	assert len(posts) == 1
	assert len(messages) == 1
