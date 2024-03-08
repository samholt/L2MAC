import pytest
from contacts import Contact

def test_contact_block_unblock():
	contact = Contact('Test')
	contact.block_contact()
	assert contact.blocked == True
	contact.unblock_contact()
	assert contact.blocked == False

def test_contact_groups():
	contact = Contact('Test')
	contact.create_group('Group1', ['Contact1', 'Contact2'])
	assert len(contact.groups) == 1
	assert contact.groups[0]['group_name'] == 'Group1'
	assert 'Contact1' in contact.groups[0]['contacts']
	assert 'Contact2' in contact.groups[0]['contacts']
	contact.edit_group('Group1', ['Contact3'])
	assert 'Contact3' in contact.groups[0]['contacts']
	assert 'Contact1' not in contact.groups[0]['contacts']
	assert 'Contact2' not in contact.groups[0]['contacts']
