import pytest
from guests import Guest

def test_guest_management():
	guest_manager = Guest()
	guest_manager.create_guest('1', 'John Doe', 'johndoe@example.com', '1234567890')
	assert guest_manager.view_guests() == {'1': {'name': 'John Doe', 'email': 'johndoe@example.com', 'phone': '1234567890', 'rsvp': False}}
	guest_manager.update_guest('1', name='Jane Doe')
	assert guest_manager.view_guests() == {'1': {'name': 'Jane Doe', 'email': 'johndoe@example.com', 'phone': '1234567890', 'rsvp': False}}
	guest_manager.track_rsvp('1', True)
	assert guest_manager.view_guests() == {'1': {'name': 'Jane Doe', 'email': 'johndoe@example.com', 'phone': '1234567890', 'rsvp': True}}
