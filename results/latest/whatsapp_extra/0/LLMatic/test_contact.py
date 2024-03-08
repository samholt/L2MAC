import pytest
from user import User
from contact import Contact

def test_block_unblock_contact():
	user1 = User('user1@example.com', 'password')
	user2 = User('user2@example.com', 'password')
	contact = Contact(user1)
	contact.block_contact(user2)
	assert user2 in contact.blocked_contacts
	contact.unblock_contact(user2)
	assert user2 not in contact.blocked_contacts

def test_group_management():
	user = User('user@example.com', 'password')
	contact = Contact(user)
	group = {'name': 'group', 'admin': user}
	contact.create_group(group)
	assert group in contact.groups
	new_group = {'name': 'new_group', 'admin': user}
	contact.edit_group(group, new_group)
	assert new_group in contact.groups
	assert group not in contact.groups
	contact.delete_group(new_group)
	assert new_group not in contact.groups
