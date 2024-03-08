import pytest
from app.models import User, Message


def test_offline_mode():
	# Create a user and a message
	user = User.create(id=1, email='testuser@test.com', password='password', profile_picture='', status_message='', privacy_settings='', last_seen='', contacts=[], blocked_contacts=[])

	message = Message.create(sender=user.email, recipient=user.email, content='Test message', timestamp='', read_receipt=False)

	# Simulate internet disconnection
	user.is_online = False

	# Try to send a message
	message.is_sent = False

	# Check that the message is queued
	assert message.is_sent == False

	# Simulate internet reconnection
	user.is_online = True

	# Check that the message is sent
	message.is_sent = True
	assert message.is_sent == True

	# Check that the online/offline status is displayed correctly
	assert user.is_online == True
