from group_chat import GroupChat
from user import User

def test_group_chat():
	group = GroupChat('Friends', 'admin@test.com')
	assert group.name == 'Friends'
	assert group.admins == ['admin@test.com']
	group.add_participant('user@test.com')
	assert 'user@test.com' in group.participants
	group.remove_participant('user@test.com')
	assert 'user@test.com' not in group.participants
	group.add_admin('user@test.com')
	assert 'user@test.com' in group.admins
	assert 'user@test.com' not in group.participants
	group.remove_admin('user@test.com')
	assert 'user@test.com' not in group.admins
	assert 'user@test.com' in group.participants

def test_user_group_management():
	user = User('test@test.com', 'password')
	user.create_group('Friends')
	assert 'Friends' in user.groups
	user.add_to_group('Friends', 'friend@test.com')
	assert 'friend@test.com' in user.groups['Friends'].participants
	user.remove_from_group('Friends', 'friend@test.com')
	assert 'friend@test.com' not in user.groups['Friends'].participants
	user.set_group_admin('Friends', 'friend@test.com')
	assert 'friend@test.com' in user.groups['Friends'].admins
	assert 'friend@test.com' not in user.groups['Friends'].participants
	user.remove_group_admin('Friends', 'friend@test.com')
	assert 'friend@test.com' not in user.groups['Friends'].admins
	assert 'friend@test.com' in user.groups['Friends'].participants
