import pytest
from contact import ContactService

def test_block_unblock_contact():
	contact_service = ContactService()
	user_id = 1
	contact_id = 2
	assert contact_service.block_contact(user_id, contact_id) == True
	assert contact_service.unblock_contact(user_id, contact_id) == True
