import pytest
from contact_service import ContactService

@pytest.fixture

def contact_service():
	return ContactService()

def test_block_unblock_contact(contact_service):
	user_id = 1
	contact_id = 2
	assert contact_service.block_contact(user_id, contact_id) == True
	assert contact_service.unblock_contact(user_id, contact_id) == True
