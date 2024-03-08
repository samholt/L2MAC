import pytest
from guest_list_management import GuestList

def test_guest_list_management():
	guest_list = GuestList()
	guest_list.add_guest('1', {'name': 'John Doe', 'rsvp': 'No'})
	assert guest_list.export_guests() == {'1': {'name': 'John Doe', 'rsvp': 'No'}}
	guest_list.update_guest('1', {'name': 'John Doe', 'rsvp': 'Yes'})
	assert guest_list.export_guests() == {'1': {'name': 'John Doe', 'rsvp': 'Yes'}}
	guest_list.import_guests({'2': {'name': 'Jane Doe', 'rsvp': 'No'}})
	assert guest_list.export_guests() == {'2': {'name': 'Jane Doe', 'rsvp': 'No'}}
	guest_list.track_rsvp('2', 'Yes')
	assert guest_list.export_guests() == {'2': {'name': 'Jane Doe', 'rsvp': 'Yes'}}
