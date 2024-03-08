import pytest
from group_chat import GroupChat

def test_group_chat():
	group_chat = GroupChat('Test Group', 'test.jpg', ['User1', 'User2'], {'User1': 'admin'})
	assert group_chat.name == 'Test Group'
	assert group_chat.picture == 'test.jpg'
	assert group_chat.participants == ['User1', 'User2']
	assert group_chat.admin_roles == {'User1': 'admin'}

	group_chat.add_participant('User3')
	assert 'User3' in group_chat.participants

	group_chat.remove_participant('User1')
	assert 'User1' not in group_chat.participants

	group_chat.set_admin_role('User2', 'admin')
	assert group_chat.admin_roles['User2'] == 'admin'

	group_chat.remove_admin_role('User1')
	assert 'User1' not in group_chat.admin_roles
