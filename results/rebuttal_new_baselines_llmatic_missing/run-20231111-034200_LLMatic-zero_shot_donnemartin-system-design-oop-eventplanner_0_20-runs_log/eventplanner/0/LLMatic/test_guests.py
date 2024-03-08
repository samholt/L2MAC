import pytest
from guests import GuestList

def test_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('1', {'name': 'John Doe', 'rsvp': 'No'})
	assert guest_list.get_guest('1') == {'name': 'John Doe', 'rsvp': 'No'}
	guest_list.remove_guest('1')
	assert guest_list.get_guest('1') is None
	guest_list.import_guest_list({'2': {'name': 'Jane Doe', 'rsvp': 'Yes'}})
	assert guest_list.get_guest('2') == {'name': 'Jane Doe', 'rsvp': 'Yes'}
	assert guest_list.export_guest_list() == {'2': {'name': 'Jane Doe', 'rsvp': 'Yes'}}
	guest_list.track_rsvp('2', 'No')
	assert guest_list.get_guest('2') == {'name': 'Jane Doe', 'rsvp': 'No'}
