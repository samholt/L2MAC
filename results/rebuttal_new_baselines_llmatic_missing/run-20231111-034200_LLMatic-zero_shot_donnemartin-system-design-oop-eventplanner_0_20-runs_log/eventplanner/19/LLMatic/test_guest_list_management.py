import pytest
from guest_list_management import GuestListManagement

def test_guest_list_management():
	guest_list_management = GuestListManagement()
	event_id = 'event1'
	guest_list = [{'name': 'John Doe', 'rsvp': 'Yes'}, {'name': 'Jane Doe', 'rsvp': 'No'}]

	# Test creating a guest list
	guest_list_management.create_guest_list(event_id, guest_list)
	assert guest_list_management.get_guest_list(event_id) == guest_list

	# Test updating a guest list
	updated_guest_list = [{'name': 'John Doe', 'rsvp': 'No'}, {'name': 'Jane Doe', 'rsvp': 'Yes'}]
	guest_list_management.update_guest_list(event_id, updated_guest_list)
	assert guest_list_management.get_guest_list(event_id) == updated_guest_list

	# Test deleting a guest list
	guest_list_management.delete_guest_list(event_id)
	assert guest_list_management.get_guest_list(event_id) == []

	# Test importing a guest list
	imported_guest_list = [{'name': 'Alice', 'rsvp': 'Yes'}, {'name': 'Bob', 'rsvp': 'No'}]
	guest_list_management.import_guest_list(event_id, imported_guest_list)
	assert guest_list_management.get_guest_list(event_id) == imported_guest_list

	# Test exporting a guest list
	assert guest_list_management.export_guest_list(event_id) == imported_guest_list

	# Test tracking RSVP
	guest_list_management.track_rsvp(event_id, 'Alice', 'No')
	assert guest_list_management.get_guest_list(event_id)[0]['rsvp'] == 'No'
