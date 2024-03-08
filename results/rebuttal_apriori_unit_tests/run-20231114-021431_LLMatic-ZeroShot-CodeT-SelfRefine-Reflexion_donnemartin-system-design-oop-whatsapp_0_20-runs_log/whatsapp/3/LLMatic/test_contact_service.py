import pytest
import random
from contact_service import ContactService


@pytest.fixture
def contact_service():
    return ContactService()


def test_block_unblock_contact(contact_service):
    user_id = random.randint(1, 100)
    contact_id = random.randint(1, 100)
    assert contact_service.block_contact(user_id, contact_id) == True
    assert contact_service.unblock_contact(user_id, contact_id) == True


def test_create_edit_group(contact_service):
    user_id = random.randint(1, 100)
    group_name = f"Group {random.randint(1, 100)}"
    group_id = contact_service.create_group(user_id, group_name)
    assert group_id is not None

    new_group_name = f"Group {random.randint(101, 200)}"
    assert contact_service.edit_group(user_id, group_id, new_group_name) == True


def test_manage_group_members(contact_service):
    user_id = random.randint(1, 100)
    group_id = contact_service.create_group(user_id, 'Test Group')
    member_id = random.randint(1, 100)
    assert contact_service.add_member_to_group(user_id, group_id, member_id) == True
    assert contact_service.remove_member_from_group(user_id, group_id, member_id) == True
