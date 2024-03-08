import pytest
from services.contact import block_contact, unblock_contact, get_contact

def test_block_contact():
	contact = block_contact(1, 2)
	assert contact.blocked == True

def test_unblock_contact():
	contact = block_contact(1, 2)
	contact = unblock_contact(1, 2)
	contact = get_contact(1, 2)
	assert contact.blocked == False

def test_get_contact():
	contact = get_contact(1, 2)
	assert contact is not None
