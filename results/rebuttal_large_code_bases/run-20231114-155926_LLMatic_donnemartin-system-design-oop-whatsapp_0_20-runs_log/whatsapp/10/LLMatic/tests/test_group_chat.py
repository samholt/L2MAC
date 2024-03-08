import pytest
from app.models import User, Group, Message
from app.views import users_db, groups_db, messages_db


def test_group_chat():
	# Create users
	user1 = User.create(id=1, email='user1@example.com', password='test', profile_picture='user1.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['user2', 'user3'], blocked_contacts=[])
	user2 = User.create(id=2, email='user2@example.com', password='test', profile_picture='user2.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['user1', 'user3'], blocked_contacts=[])
	user3 = User.create(id=3, email='user3@example.com', password='test', profile_picture='user3.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['user1', 'user2'], blocked_contacts=[])
	users_db[user1.id] = user1
	users_db[user2.id] = user2
	users_db[user3.id] = user3

	# Create a group
	group = Group.create(name='group1', picture='group1.jpg', members=[user1.email, user2.email])
	groups_db[group.name] = group

	# Add a member to the group
	group.members.append(user3.email)
	assert user3.email in group.members

	# Remove a member from the group
	group.members.remove(user2.email)
	assert user2.email not in group.members

	# Send a message in the group
	message = Message.create(sender=user1.email, recipient=group.name, content='Hello, group!', timestamp='2022-01-01 00:00:00', read_receipt=False)
	messages_db[(user1.email, group.name)] = [message]
	assert message in messages_db[(user1.email, group.name)]

	# Read a message in the group
	message.read_receipt = True
	assert message.read_receipt is True

