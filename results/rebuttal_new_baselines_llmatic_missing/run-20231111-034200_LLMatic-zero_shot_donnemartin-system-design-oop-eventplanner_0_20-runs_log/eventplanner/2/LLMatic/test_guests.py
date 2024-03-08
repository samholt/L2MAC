import pytest
from guests import GuestList

def test_guest_list():
	gl = GuestList()
	gl.add_guest('event1', {'name': 'John Doe', 'rsvp': 'No'})
	assert gl.get_guest_list('event1') == [{'name': 'John Doe', 'rsvp': 'No'}]
	gl.import_guest_list('event1', [{'name': 'Jane Doe', 'rsvp': 'Yes'}, {'name': 'Jim Doe', 'rsvp': 'No'}])
	assert gl.get_guest_list('event1') == [{'name': 'John Doe', 'rsvp': 'No'}, {'name': 'Jane Doe', 'rsvp': 'Yes'}, {'name': 'Jim Doe', 'rsvp': 'No'}]
	assert gl.export_guest_list('event1') == [{'name': 'John Doe', 'rsvp': 'No'}, {'name': 'Jane Doe', 'rsvp': 'Yes'}, {'name': 'Jim Doe', 'rsvp': 'No'}]
	gl.track_rsvp('event1', {'name': 'John Doe', 'rsvp': 'No'}, 'Yes')
	assert gl.get_guest_list('event1') == [{'name': 'John Doe', 'rsvp': 'Yes'}, {'name': 'Jane Doe', 'rsvp': 'Yes'}, {'name': 'Jim Doe', 'rsvp': 'No'}]
