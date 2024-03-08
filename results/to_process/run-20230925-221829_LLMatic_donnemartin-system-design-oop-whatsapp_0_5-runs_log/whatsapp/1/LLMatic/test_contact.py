import pytest
from contact import Contact
from user import User

def test_block_unblock_contact():
	contact = Contact()
	user = User('test_user', 'password')
	contact.block_contact(user)
	assert user in contact.blocked_contacts
	contact.unblock_contact(user)
	assert user not in contact.blocked_contacts

def test_group_management():
	contact = Contact()
	group_name = 'test_group'
	user = User('test_user', 'password')
	contact.create_group(group_name)
	assert group_name in contact.groups
	contact.add_user_to_group(group_name, user)
	assert user in contact.groups[group_name]
	contact.remove_user_from_group(group_name, user)
	assert user not in contact.groups[group_name]
