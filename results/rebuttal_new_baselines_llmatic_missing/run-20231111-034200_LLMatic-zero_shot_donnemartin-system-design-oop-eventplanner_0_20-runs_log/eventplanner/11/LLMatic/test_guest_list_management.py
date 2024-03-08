import pytest
from guest_list_management import GuestListManagement

def test_guest_list_management():
	gl = GuestListManagement()
	gl.create_guest_list('event1')
	gl.add_guest('event1', {'name': 'John Doe', 'rsvp': 'No'})
	assert len(gl.get_guest_list('event1')) == 1
	gl.remove_guest('event1', {'name': 'John Doe', 'rsvp': 'No'})
	assert len(gl.get_guest_list('event1')) == 0
	gl.import_guest_list('event1', [{'name': 'Jane Doe', 'rsvp': 'Yes'}])
	assert len(gl.get_guest_list('event1')) == 1
	assert gl.export_guest_list('event1') == [{'name': 'Jane Doe', 'rsvp': 'Yes'}]
	gl.track_rsvp('event1', {'name': 'Jane Doe', 'rsvp': 'Yes'}, 'No')
	assert gl.get_guest_list('event1')[0]['rsvp'] == 'No'
