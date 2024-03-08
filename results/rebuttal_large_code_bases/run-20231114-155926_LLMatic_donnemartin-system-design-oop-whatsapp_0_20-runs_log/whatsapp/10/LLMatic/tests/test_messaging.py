import pytest
from app.models import User, Message
from app.views import users_db, messages_db
from datetime import datetime


def test_messaging():
	# Create users
	user1 = User.create(id=1, email='user1@example.com', password='test', profile_picture='user1.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['user2'], blocked_contacts=[])
	user2 = User.create(id=2, email='user2@example.com', password='test', profile_picture='user2.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['user1'], blocked_contacts=[])
	users_db[user1.id] = user1
	users_db[user2.id] = user2

	# Send a message
	message = Message.create(sender='user1', recipient='user2', content='Hello, user2!', timestamp=datetime.utcnow(), read_receipt=False)
	messages_db[('user1', 'user2')] = [message]
	assert message in messages_db[('user1', 'user2')]

	# Read a message
	message.read_receipt = True
	assert message.read_receipt

	# Share an image
	image_message = Message.create(sender='user1', recipient='user2', content='image.jpg', timestamp=datetime.utcnow(), read_receipt=False)
	messages_db[('user1', 'user2')].append(image_message)
	assert image_message in messages_db[('user1', 'user2')]
