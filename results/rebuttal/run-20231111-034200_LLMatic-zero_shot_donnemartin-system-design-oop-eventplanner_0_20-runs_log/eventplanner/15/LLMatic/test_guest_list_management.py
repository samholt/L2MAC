import guest_list_management

def test_guest_list_management():
	guest_list = guest_list_management.GuestList()
	guest_list.add_guest('John Doe', 'johndoe@example.com')
	assert 'johndoe@example.com' in guest_list.export_guest_list()
	guest_list.remove_guest('johndoe@example.com')
	assert 'johndoe@example.com' not in guest_list.export_guest_list()
	guest_list.import_guest_list({'janedoe@example.com': {'name': 'Jane Doe', 'RSVP': False}})
	assert 'janedoe@example.com' in guest_list.export_guest_list()
	guest_list.update_rsvp('janedoe@example.com', True)
	assert guest_list.export_guest_list()['janedoe@example.com']['RSVP'] == True
