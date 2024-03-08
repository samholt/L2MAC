import pytest
from user import User
from contact import Contact

def test_contact():
	user = User('test@example.com', 'password')
	contact = Contact(user)
	assert contact.user == user
	assert contact.blocked_contacts == []
	assert contact.groups == []

	contact.block_contact('blocked@example.com')
	assert 'blocked@example.com' in contact.blocked_contacts

	contact.unblock_contact('blocked@example.com')
	assert 'blocked@example.com' not in contact.blocked_contacts

	contact.create_group('Test Group')
	assert any(group['name'] == 'Test Group' for group in contact.groups)

	contact.edit_group('Test Group', 'New Test Group')
	assert any(group['name'] == 'New Test Group' for group in contact.groups)

	contact.manage_group('New Test Group', 'add', 'member@example.com')
	assert any('member@example.com' in group['members'] for group in contact.groups if group['name'] == 'New Test Group')

	contact.manage_group('New Test Group', 'remove', 'member@example.com')
	assert not any('member@example.com' in group['members'] for group in contact.groups if group['name'] == 'New Test Group')
