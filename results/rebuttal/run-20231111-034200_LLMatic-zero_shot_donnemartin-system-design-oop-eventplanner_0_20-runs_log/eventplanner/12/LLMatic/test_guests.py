import pytest
from guests import Guest, GuestList

def test_guest_creation():
	guest = Guest('John Doe', 'Yes')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'

def test_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	guest = guest_list.get_guest('John Doe')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'

def test_import_export_guests():
	guest_list = GuestList()
	guest_list.import_guests([{'name': 'John Doe', 'rsvp_status': 'Yes'}])
	exported_guests = guest_list.export_guests()
	assert exported_guests == [{'name': 'John Doe', 'rsvp_status': 'Yes'}]

def test_manage_guest():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	guest_list.manage_guest('John Doe', 'No')
	guest = guest_list.get_guest('John Doe')
	assert guest.rsvp_status == 'No'
