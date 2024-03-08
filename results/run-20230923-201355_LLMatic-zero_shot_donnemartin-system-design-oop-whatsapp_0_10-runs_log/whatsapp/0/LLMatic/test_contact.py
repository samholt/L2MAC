import pytest
from user import User
from contact import Contact
from group import Group


def test_contact():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	contact = Contact(user1)
	group = Group('Test Group', 'test.jpg', [], [], [])

	# Test block_contact
	contact.block_contact(user2)
	assert user2 in contact.blocked_contacts

	# Test unblock_contact
	contact.unblock_contact(user2)
	assert user2 not in contact.blocked_contacts

	# Test create_group
	contact.create_group(group)
	assert group in contact.groups

	# Test edit_group
	new_group = Group('New Test Group', 'new_test.jpg', [], [], [])
	contact.edit_group(group, new_group)
	assert new_group in contact.groups
	assert group not in contact.groups

	# Test manage_group
	managed_group = contact.manage_group(new_group)
	assert managed_group == new_group
