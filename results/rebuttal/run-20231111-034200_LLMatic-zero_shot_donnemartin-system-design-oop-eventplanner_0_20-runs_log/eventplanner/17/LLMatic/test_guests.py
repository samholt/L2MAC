import pytest
from guests import GuestList

def test_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('event1', 'John Doe')
	assert 'John Doe' in guest_list.get_guest_list('event1')
	guest_list.remove_guest('event1', 'John Doe')
	assert 'John Doe' not in guest_list.get_guest_list('event1')
	guest_list.import_guest_list('event1', ['Jane Doe', 'John Smith'])
	assert 'Jane Doe' in guest_list.get_guest_list('event1')
	assert 'John Smith' in guest_list.get_guest_list('event1')
	exported_list = guest_list.export_guest_list('event1')
	assert 'Jane Doe' in exported_list
	assert 'John Smith' in exported_list
	guest_list.track_rsvp('event1', 'Jane Doe', 'Yes')
	assert ('Jane Doe', 'Yes') in guest_list.get_guest_list('event1')
