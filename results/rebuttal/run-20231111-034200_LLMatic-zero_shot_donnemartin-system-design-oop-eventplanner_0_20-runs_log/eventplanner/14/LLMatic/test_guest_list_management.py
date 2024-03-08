import pytest
from guest_list_management import Guest, GuestList


def test_guest_creation():
	guest = Guest('John Doe', 'Yes')
	assert guest.name == 'John Doe'
	assert guest.rsvp_status == 'Yes'


def test_guest_list_creation():
	guest_list = GuestList()
	assert guest_list.guest_list == {}


def test_add_guest():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	assert 'John Doe' in guest_list.guest_list
	assert guest_list.guest_list['John Doe'].rsvp_status == 'Yes'


def test_update_guest():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	guest_list.update_guest('John Doe', 'No')
	assert guest_list.guest_list['John Doe'].rsvp_status == 'No'


def test_view_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	assert guest_list.view_guest_list() == {'John Doe': 'Yes'}


def test_import_export_guest_list():
	guest_list = GuestList()
	guest_list.add_guest('John Doe', 'Yes')
	guest_list.export_guest_list('test_guest_list.txt')
	new_guest_list = GuestList()
	new_guest_list.import_guest_list('test_guest_list.txt')
	assert new_guest_list.view_guest_list() == {'John Doe': 'Yes'}
