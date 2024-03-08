import pytest
from group_chat import GroupChat


def test_group_chat():
	group_chat = GroupChat('Test Group')
	group_chat.create_group_chat('Test Group', 'test.jpg', ['user1', 'user2'], ['admin1'])
	assert group_chat.name == 'Test Group'
	assert group_chat.picture == 'test.jpg'
	assert group_chat.participants == ['user1', 'user2']
	assert group_chat.admins == ['admin1']

	group_chat.add_participant('user3')
	assert 'user3' in group_chat.participants

	group_chat.remove_participant('user1')
	assert 'user1' not in group_chat.participants

	group_chat.manage_admin_roles('admin2')
	assert 'admin2' in group_chat.admins

	group_chat.manage_admin_roles('admin1')
	assert 'admin1' not in group_chat.admins
