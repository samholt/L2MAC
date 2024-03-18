from user import User

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
