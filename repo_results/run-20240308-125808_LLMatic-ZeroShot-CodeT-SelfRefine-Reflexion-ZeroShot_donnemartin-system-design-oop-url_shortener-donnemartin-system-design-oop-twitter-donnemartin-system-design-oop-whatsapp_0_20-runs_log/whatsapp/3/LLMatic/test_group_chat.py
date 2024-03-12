import pytest
from group_chat import GroupChat

def test_group_chat():
	group = GroupChat('group1', 'admin1')
	assert group.group_id == 'group1'
	assert group.admin == 'admin1'
	assert group.participants == {'admin1': 'admin'}
	group.add_participant('user1')
	assert group.participants == {'admin1': 'admin', 'user1': 'participant'}
	group.remove_participant('user1')
	assert group.participants == {'admin1': 'admin'}
	group.add_participant('user1')
	group.set_admin('user1')
	assert group.participants == {'admin1': 'admin', 'user1': 'admin'}
	group.remove_admin('user1')
	assert group.participants == {'admin1': 'admin', 'user1': 'participant'}
