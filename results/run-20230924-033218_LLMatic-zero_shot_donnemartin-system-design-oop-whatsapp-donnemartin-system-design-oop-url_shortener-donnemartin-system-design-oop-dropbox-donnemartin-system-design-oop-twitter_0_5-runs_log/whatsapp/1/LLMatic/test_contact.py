import pytest
from user import User
from contact import Contact

def test_block_unblock_contact():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	contact = Contact(user1)
	assert contact.block_contact(user2) == 'Contact blocked successfully'
	assert contact.block_contact(user2) == 'Contact already blocked'
	assert contact.unblock_contact(user2) == 'Contact unblocked successfully'
	assert contact.unblock_contact(user2) == 'Contact not found in blocked list'

def test_group_management():
	user = User('user@example.com', 'password')
	contact = Contact(user)
	group = 'group1'
	new_group = 'group2'
	assert contact.create_group(group) == 'Group created successfully'
	assert contact.create_group(group) == 'Group already exists'
	assert contact.edit_group(group, new_group) == 'Group edited successfully'
	assert contact.edit_group(group, new_group) == 'Group not found'
	assert contact.manage_group(new_group) == 'Group managed'
	assert contact.manage_group(group) == 'Group not found'
