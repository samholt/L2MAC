import pytest
from guest_list_management import Guest, GuestListManagement

def test_guest_creation():
	guest = Guest('John Doe', 'Yes')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'

def test_guest_list_management():
	gl = GuestListManagement()
	guest = Guest('John Doe', 'Yes')
	gl.add_guest(guest)
	assert gl.view_guest_list() == {'John Doe': 'Yes'}
	gl.update_guest('John Doe', 'No')
	assert gl.view_guest_list() == {'John Doe': 'No'}
	gl.import_guest_list({'Jane Doe': 'Yes'})
	assert gl.view_guest_list() == {'Jane Doe': 'Yes'}
	exported_list = gl.export_guest_list()
	assert exported_list == {'Jane Doe': 'Yes'}
