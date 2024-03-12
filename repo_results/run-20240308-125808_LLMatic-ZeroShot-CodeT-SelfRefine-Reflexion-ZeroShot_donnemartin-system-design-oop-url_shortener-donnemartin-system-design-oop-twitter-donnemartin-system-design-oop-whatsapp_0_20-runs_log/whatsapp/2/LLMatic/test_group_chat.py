import pytest
from group_chat import GroupChat

def test_group_chat():
	group_chat = GroupChat('test_group', 'admin@test.com')
	assert group_chat.group_name == 'test_group'
	assert group_chat.admin == 'admin@test.com'
	assert group_chat.participants == {'admin@test.com': 'admin'}

	group_chat.add_participant('participant@test.com')
	assert group_chat.participants == {'admin@test.com': 'admin', 'participant@test.com': 'participant'}

	group_chat.remove_participant('participant@test.com')
	assert group_chat.participants == {'admin@test.com': 'admin'}

	group_chat.add_participant('participant@test.com')
	group_chat.set_admin('participant@test.com')
	assert group_chat.participants == {'admin@test.com': 'admin', 'participant@test.com': 'admin'}

	assert group_chat.get_participants() == {'admin@test.com': 'admin', 'participant@test.com': 'admin'}
