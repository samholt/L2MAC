import pytest
from user import User, Contact


def test_block_contact():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	contact = Contact(user2)
	assert contact.block_contact(user2) == 'Contact blocked successfully'
	assert contact.blocked == True


def test_unblock_contact():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	contact = Contact(user2, blocked=True)
	assert contact.unblock_contact(user2) == 'Contact unblocked successfully'
	assert contact.blocked == False


def test_create_group():
	user = User('user@example.com', 'password')
	contact = Contact(user)
	group_details = {'name': 'Group 1', 'members': [user]}
	assert contact.create_group(group_details) == 'Group created successfully'


def test_edit_group():
	user = User('user@example.com', 'password')
	contact = Contact(user)
	group_details = {'name': 'Group 1', 'members': [user]}
	contact.create_group(group_details)
	new_group_details = {'name': 'Group 1 edited', 'members': [user]}
	assert contact.edit_group(new_group_details) == 'Group edited successfully'


def test_manage_group():
	user = User('user@example.com', 'password')
	contact = Contact(user)
	group_details = {'name': 'Group 1', 'members': [user]}
	contact.create_group(group_details)
	new_group_details = {'name': 'Group 1 managed', 'members': [user]}
	assert contact.manage_group(new_group_details) == 'Group managed successfully'
