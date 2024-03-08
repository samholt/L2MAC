import pytest
from guest_list_management import GuestList

def test_guest_list_management():
	guest_list = GuestList()
	guest_list.add_guest('John Doe')
	assert 'John Doe' in guest_list.export_guests()
	guest_list.update_guest('John Doe', 'Confirmed')
	assert guest_list.export_guests()['John Doe'] == 'Confirmed'
	guest_list.import_guests(['Jane Doe', 'Richard Roe'])
	assert 'Jane Doe' in guest_list.export_guests()
	assert 'Richard Roe' in guest_list.export_guests()
	assert guest_list.track_rsvps() == {'Pending': ['Jane Doe', 'Richard Roe'], 'Confirmed': ['John Doe']}
