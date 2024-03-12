import pytest
from group import Group
from contact import Contact

def test_create_group():
	group = Group('Test Group', 'test.jpg')
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'

def test_add_remove_contact():
	group = Group('Test Group')
	contact = Contact('Test Contact')
	group.add_contact(contact)
	assert contact in group.contacts
	group.remove_contact(contact)
	assert contact not in group.contacts

def test_admin_roles():
	group = Group('Test Group')
	contact = Contact('Test Contact')
	group.add_admin(contact)
	assert contact in group.admins
	group.remove_admin(contact)
	assert contact not in group.admins
