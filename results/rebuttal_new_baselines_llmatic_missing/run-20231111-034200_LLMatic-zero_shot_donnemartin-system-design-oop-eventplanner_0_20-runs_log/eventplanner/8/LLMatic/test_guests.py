from guests import Guest, GuestList

def test_guest():
	guest = Guest('John Doe', 'johndoe@example.com')
	assert guest.name == 'John Doe'
	assert guest.email == 'johndoe@example.com'
	assert not guest.rsvp_status
	guest.rsvp()
	assert guest.rsvp_status

def test_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'johndoe@example.com')
	guest = guest_list.get_guest('johndoe@example.com')
	assert guest is not None
	assert guest.name == 'John Doe'
	assert guest.email == 'johndoe@example.com'
	guest_list.remove_guest('johndoe@example.com')
	assert guest_list.get_guest('johndoe@example.com') is None

def test_import_export_guests():
	guest_list = GuestList()
	guest_list.import_guests([{'name': 'John Doe', 'email': 'johndoe@example.com'}])
	exported_guests = guest_list.export_guests()
	assert len(exported_guests) == 1
	assert exported_guests[0]['name'] == 'John Doe'
	assert exported_guests[0]['email'] == 'johndoe@example.com'

def test_track_rsvps():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'johndoe@example.com')
	guest = guest_list.get_guest('johndoe@example.com')
	guest.rsvp()
	rsvps = guest_list.track_rsvps()
	assert rsvps['johndoe@example.com']
