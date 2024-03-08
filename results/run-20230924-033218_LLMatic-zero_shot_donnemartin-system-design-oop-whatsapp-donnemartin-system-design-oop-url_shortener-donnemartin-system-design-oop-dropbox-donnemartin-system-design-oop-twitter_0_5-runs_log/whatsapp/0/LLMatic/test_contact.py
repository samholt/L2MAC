import pytest
from contact import Contact

def test_block():
	contact = Contact('Test', 'test@test.com', 'picture.jpg', 'Hello', '2022-01-01 00:00:00', False)
	contact.block()
	assert contact.blocked == True

def test_unblock():
	contact = Contact('Test', 'test@test.com', 'picture.jpg', 'Hello', '2022-01-01 00:00:00', True)
	contact.unblock()
	assert contact.blocked == False

def test_view_profile():
	contact = Contact('Test', 'test@test.com', 'picture.jpg', 'Hello', '2022-01-01 00:00:00', False)
	profile = contact.view_profile()
	assert profile == {'name': 'Test', 'email': 'test@test.com', 'profile_picture': 'picture.jpg', 'status_message': 'Hello', 'last_seen': '2022-01-01 00:00:00'}

def test_view_status():
	contact = Contact('Test', 'test@test.com', 'picture.jpg', 'Hello', '2022-01-01 00:00:00', False)
	status = contact.view_status()
	assert status == 'Hello'

def test_send_message():
	contact = Contact('Test', 'test@test.com', 'picture.jpg', 'Hello', '2022-01-01 00:00:00', False)
	message = contact.send_message('Hello Test')
	assert message == 'Message sent to Test: Hello Test'

	contact.block()
	message = contact.send_message('Hello Test')
	assert message == 'Contact is blocked, message not sent.'
