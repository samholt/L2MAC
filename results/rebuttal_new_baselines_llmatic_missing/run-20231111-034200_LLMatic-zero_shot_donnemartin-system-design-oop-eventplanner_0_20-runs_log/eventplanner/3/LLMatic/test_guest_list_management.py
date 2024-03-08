import pytest
from guest_list_management import Guest, GuestListManagement

def test_guest_creation():
	guest = Guest('John Doe', 'Yes')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'

def test_guest_list_management():
	gl = GuestListManagement()
	gl.add_guest(Guest('John Doe', 'Yes'))
	assert gl.get_guest('John Doe') == 'Yes'
	gl.update_guest('John Doe', 'No')
	assert gl.get_guest('John Doe') == 'No'
	gl.remove_guest('John Doe')
	assert gl.get_guest('John Doe') is None

def test_import_export_guest_list():
	gl = GuestListManagement()
	gl.import_guest_list({'John Doe': 'Yes', 'Jane Doe': 'No'})
	assert gl.export_guest_list() == {'John Doe': 'Yes', 'Jane Doe': 'No'}
