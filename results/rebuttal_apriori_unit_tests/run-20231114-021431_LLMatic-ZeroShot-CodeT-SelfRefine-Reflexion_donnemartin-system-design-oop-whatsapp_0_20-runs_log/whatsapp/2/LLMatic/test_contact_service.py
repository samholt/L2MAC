import pytest
import random

from contact_service import ContactService

contact_service = ContactService()

user_id = random.randint(1, 100)
contacts_list = [random.randint(1, 100) for _ in range(10)]


def test_block_unblock_contact():
	contact_id = random.choice(contacts_list)
	assert contact_service.block_contact(user_id, contact_id) == True
	assert contact_service.unblock_contact(user_id, contact_id) == True
