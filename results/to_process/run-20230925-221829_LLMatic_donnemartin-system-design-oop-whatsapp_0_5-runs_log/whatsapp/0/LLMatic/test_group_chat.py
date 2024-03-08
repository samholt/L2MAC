import pytest
from group_chat import GroupChat

def test_group_chat():
	group_chat = GroupChat()
	group_chat_id = group_chat.create_group_chat('user1', 'group1', 'picture1', ['user2', 'user3'])
	assert group_chat_id == 1
	assert group_chat.group_chats[group_chat_id]['name'] == 'group1'
	assert group_chat.group_chats[group_chat_id]['picture'] == 'picture1'
	assert group_chat.group_chats[group_chat_id]['participants'] == ['user2', 'user3']
	assert group_chat.group_chats[group_chat_id]['roles']['user1'] == 'admin'

	group_chat.add_participant(group_chat_id, 'user4')
	assert 'user4' in group_chat.group_chats[group_chat_id]['participants']

	group_chat.remove_participant(group_chat_id, 'user2')
	assert 'user2' not in group_chat.group_chats[group_chat_id]['participants']

	group_chat.manage_roles(group_chat_id, 'user3', 'admin')
	assert group_chat.group_chats[group_chat_id]['roles']['user3'] == 'admin'
