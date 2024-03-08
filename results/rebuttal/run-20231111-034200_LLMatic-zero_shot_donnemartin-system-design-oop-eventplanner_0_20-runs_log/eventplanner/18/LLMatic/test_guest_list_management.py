from guest_list_management import Guest, GuestList

def test_guest_creation():
	guest = Guest('John Doe', 'Yes')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'

def test_guest_list_management():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	assert guest_list.guest_list['John Doe'].name == 'John Doe'
	assert guest_list.guest_list['John Doe'].rsvp_status == 'Yes'
	guest_list.update_guest('John Doe', 'No')
	assert guest_list.guest_list['John Doe'].rsvp_status == 'No'

def test_guest_list_import_export():
	guest_list = GuestList()
	guest_list.import_guest_list([{'name': 'John Doe', 'rsvp_status': 'Yes'}])
	assert guest_list.guest_list['John Doe'].name == 'John Doe'
	assert guest_list.guest_list['John Doe'].rsvp_status == 'Yes'
	exported_list = guest_list.export_guest_list()
	assert exported_list == [{'name': 'John Doe', 'rsvp_status': 'Yes'}]
