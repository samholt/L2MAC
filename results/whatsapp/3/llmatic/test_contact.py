import pytest
from contact import Contact


def test_contact_creation():
	contact = Contact()
	assert contact.blocked_contacts == []
	assert contact.groups == []


def test_block_contact():
	contact = Contact()
	contact.block_contact('test@example.com')
	assert 'test@example.com' in contact.blocked_contacts


def test_unblock_contact():
	contact = Contact()
	contact.block_contact('test@example.com')
	contact.unblock_contact('test@example.com')
	assert 'test@example.com' not in contact.blocked_contacts


def test_create_group():
	contact = Contact()
	contact.create_group('Group 1')
	assert 'Group 1' in contact.groups


def test_edit_group():
	contact = Contact()
	contact.create_group('Group 1')
	contact.edit_group('Group 1', 'Group 2')
	assert 'Group 1' not in contact.groups
	assert 'Group 2' in contact.groups


def test_manage_groups():
	contact = Contact()
	contact.create_group('Group 1')
	contact.manage_groups('Group 1')
	assert 'Group 1' not in contact.groups
