import contacts

def test_contacts():
	c = contacts.Contacts()

	# Test blocking and unblocking contacts
	c.block_contact('user1', 'contact1')
	assert 'contact1' in c.contacts_db['user1']['blocked']
	c.unblock_contact('user1', 'contact1')
	assert 'contact1' not in c.contacts_db['user1']['blocked']

	# Test creating and editing groups
	c.create_group('user1', 'group1', ['contact2', 'contact3'])
	group_id = c.contacts_db['user1']['groups'][0]
	assert c.groups_db[group_id]['name'] == 'group1'
	assert 'contact2' in c.groups_db[group_id]['contacts']
	c.edit_group(group_id, 'new_group1', ['contact4', 'contact5'])
	assert c.groups_db[group_id]['name'] == 'new_group1'
	assert 'contact4' in c.groups_db[group_id]['contacts']

	# Test managing groups
	group = c.manage_group('user1', group_id)
	assert group['name'] == 'new_group1'
	assert 'contact4' in group['contacts']
