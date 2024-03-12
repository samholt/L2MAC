import pytest
from contact import Contact, Group

def test_contact_block_unblock():
	contact = Contact('John')
	assert contact.blocked == False
	contact.block()
	assert contact.blocked == True
	contact.unblock()
	assert contact.blocked == False

def test_group():
	group = Group('Friends')
	assert group.group_name == 'Friends'
	assert group.members == []
	john = Contact('John')
	group.add_member(john)
	assert john in group.members
	group.remove_member(john)
	assert john not in group.members
	group.edit_group_name('Best Friends')
	assert group.group_name == 'Best Friends'
