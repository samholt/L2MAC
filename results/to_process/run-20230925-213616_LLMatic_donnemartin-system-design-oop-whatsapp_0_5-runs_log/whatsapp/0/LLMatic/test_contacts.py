import contacts


def test_block_unblock_contact():
	# Test blocking a contact
	contacts.block_unblock_contact('user1@example.com', 'contact1@example.com')
	assert contacts.contacts_db['contact1@example.com'].blocked == True

	# Test unblocking a contact
	contacts.block_unblock_contact('user1@example.com', 'contact1@example.com')
	assert contacts.contacts_db['contact1@example.com'].blocked == False


def test_create_group():
	# Test creating a group
	contacts.create_group('group1', 'user1@example.com')
	assert 'user1@example.com' in contacts.groups_db['group1']


def test_edit_group():
	# Test adding a user to a group
	contacts.edit_group('group1', 'user2@example.com', 'add')
	assert 'user2@example.com' in contacts.groups_db['group1']

	# Test removing a user from a group
	contacts.edit_group('group1', 'user2@example.com', 'remove')
	assert 'user2@example.com' not in contacts.groups_db['group1']

