from groups import Groups

def test_groups():
	groups = Groups()
	groups.create_group('group1', 'admin1')
	group1 = groups.get_group('group1')
	assert group1 is not None
	assert group1.admin == 'admin1'
	assert group1.members == {'admin1': 'admin'}
	group1.add_member('user1')
	assert group1.members == {'admin1': 'admin', 'user1': 'member'}
	group1.remove_member('user1')
	assert group1.members == {'admin1': 'admin'}
	group1.add_member('user1')
	group1.promote_to_admin('admin1', 'user1')
	assert group1.members == {'admin1': 'admin', 'user1': 'admin'}
	group1.demote_from_admin('admin1', 'user1')
	assert group1.members == {'admin1': 'admin', 'user1': 'member'}
	groups.delete_group('group1')
	assert groups.get_group('group1') is None
