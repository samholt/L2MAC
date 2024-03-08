import pytest
from guests import Guest
from database import Database

def test_guest_creation():
	guest = Guest('John Doe', 'johndoe@example.com', 'Not Responded')
	assert guest.get_guest_info() == {'name': 'John Doe', 'contact_info': 'johndoe@example.com', 'rsvp_status': 'Not Responded'}

def test_guest_update_rsvp_status():
	guest = Guest('John Doe', 'johndoe@example.com', 'Not Responded')
	guest.update_rsvp_status('Attending')
	assert guest.get_guest_info() == {'name': 'John Doe', 'contact_info': 'johndoe@example.com', 'rsvp_status': 'Attending'}

def test_database_guest_storage():
	db = Database()
	guest = Guest('John Doe', 'johndoe@example.com', 'Not Responded')
	db.add_guest('1', guest)
	stored_guest = db.get_guest('1')
	assert stored_guest.get_guest_info() == {'name': 'John Doe', 'contact_info': 'johndoe@example.com', 'rsvp_status': 'Not Responded'}
