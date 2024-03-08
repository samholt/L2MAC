import group

def test_create_edit_manage_group():
	g = group.Group()
	assert g.create_group('user1', 'Test Group', ['1', '2', '3', '4']) == 'Group created successfully'
	assert g.edit_group('user1', 'Test Group', 'New Test Group', ['2', '3', '4', '5']) == 'Group edited successfully'
	assert g.manage_groups('user1') == {'New Test Group': ['2', '3', '4', '5']}

def test_add_remove_participant():
	g = group.Group()
	g.create_group('user1', 'Test Group', ['1', '2', '3', '4'])
	assert g.add_participant('user1', 'Test Group', '5') == 'Participant added successfully'
	assert g.remove_participant('user1', 'Test Group', '5') == 'Participant removed successfully'

