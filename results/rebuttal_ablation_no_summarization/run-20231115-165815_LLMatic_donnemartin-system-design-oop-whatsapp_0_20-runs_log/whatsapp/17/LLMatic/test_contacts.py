from contacts import Contacts

def test_contacts():
	contacts = Contacts()
	contacts.add_contact('John')
	assert 'John' in contacts.contacts
	contacts.block_contact('John')
	assert contacts.get_contact('John').blocked
	contacts.unblock_contact('John')
	assert not contacts.get_contact('John').blocked
	contacts.add_contact_to_group('John', 'Friends')
	assert 'Friends' in contacts.get_contact('John').groups
	contacts.remove_contact_from_group('John', 'Friends')
	assert 'Friends' not in contacts.get_contact('John').groups
