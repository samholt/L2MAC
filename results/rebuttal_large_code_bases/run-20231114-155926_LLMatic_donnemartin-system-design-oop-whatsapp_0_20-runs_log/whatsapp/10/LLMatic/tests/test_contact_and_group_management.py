import pytest
from app.models import User, Group
from app.views import users_db, groups_db


def test_contact_and_group_management():
	# Create a user
	user = User.create(id=1, email='test@example.com', password='test', profile_picture='test.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=['contact1', 'contact2'], blocked_contacts=[])
	users_db[user.id] = user

	# Block a contact
	user.contacts.remove('contact1')
	user.blocked_contacts.append('contact1')
	assert 'contact1' not in user.contacts
	assert 'contact1' in user.blocked_contacts

	# Unblock a contact
	user.blocked_contacts.remove('contact1')
	user.contacts.append('contact1')
	assert 'contact1' in user.contacts
	assert 'contact1' not in user.blocked_contacts

	# Create a group
	group = Group.create(name='group1', picture='group1.jpg', members=['user1', 'user2'])
	groups_db[group.name] = group

	# Add a member to the group
	group.members.append('user3')
	assert 'user3' in group.members

	# Remove a member from the group
	group.members.remove('user2')
	assert 'user2' not in group.members
