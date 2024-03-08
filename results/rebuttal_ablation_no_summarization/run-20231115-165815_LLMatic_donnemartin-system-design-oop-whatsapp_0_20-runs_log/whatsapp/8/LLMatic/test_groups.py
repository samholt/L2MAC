import pytest
from groups import GroupChat

def test_group_chat():
	group = GroupChat('Test Group', 'test.jpg', ['User1', 'User2'])
	group_chat = group.create_group_chat()
	assert group_chat['group_name'] == 'Test Group'
	assert group_chat['group_picture'] == 'test.jpg'
	assert group_chat['participants'] == ['User1', 'User2']
	assert group_chat['admins'] == ['User1']

	group.add_participant('User3')
	assert 'User3' in group_chat['participants']

	group.remove_participant('User2')
	assert 'User2' not in group_chat['participants']

	group.manage_admin_roles('User3', 'add')
	assert 'User3' in group_chat['admins']

	group.manage_admin_roles('User1', 'remove')
	assert 'User1' not in group_chat['admins']
