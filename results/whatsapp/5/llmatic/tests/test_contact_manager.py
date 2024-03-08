import pytest
from models.user import User
from controllers.contact_manager import ContactManager

def test_contact_manager():
	user1 = User('1', 'user1@example.com', 'password1', '', '', {}, [])
	user2 = User('2', 'user2@example.com', 'password2', '', '', {}, [])
	user3 = User('3', 'user3@example.com', 'password3', '', '', {}, [])
	contact_manager = ContactManager()

	# Test create_group
	contact_manager.create_group('group1', {user1: 'admin', user2: 'member'})
	assert 'group1' in contact_manager.groups
	assert contact_manager.groups['group1'] == {user1: 'admin', user2: 'member'}

	# Test edit_group
	contact_manager.edit_group('group1', {user1: 'admin', user2: 'member', user3: 'member'})
	assert contact_manager.groups['group1'] == {user1: 'admin', user2: 'member', user3: 'member'}

	# Test manage_group
	contact_manager.manage_group('group1', user3, 'remove')
	assert contact_manager.groups['group1'] == {user1: 'admin', user2: 'member'}

	# Test set_admin
	contact_manager.set_admin('group1', user2)
	assert contact_manager.groups['group1'] == {user1: 'admin', user2: 'admin'}

	# Test remove_admin
	contact_manager.remove_admin('group1', user2)
	assert contact_manager.groups['group1'] == {user1: 'admin', user2: 'member'}
