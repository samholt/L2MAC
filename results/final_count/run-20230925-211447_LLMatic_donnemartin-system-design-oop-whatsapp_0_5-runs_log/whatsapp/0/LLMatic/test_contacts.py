import pytest
from contacts import Contacts

def test_block_unblock_contact():
	contacts = Contacts()
	contacts.block_unblock_contact('user1@example.com', 'user2@example.com')
	assert 'user2@example.com' in contacts.users['user1@example.com']['blocked_contacts']
	contacts.block_unblock_contact('user1@example.com', 'user2@example.com')
	assert 'user2@example.com' not in contacts.users['user1@example.com']['blocked_contacts']

def test_manage_group():
	contacts = Contacts()
	contacts.manage_group('user1@example.com', 'group1', ['user2@example.com', 'user3@example.com'])
	assert 'group1' in contacts.users['user1@example.com']['groups']
	assert contacts.users['user1@example.com']['groups']['group1'] == ['user2@example.com', 'user3@example.com']
