import pytest
from user import User
from profile import Profile
from contact import Contact
from message import Message
from group_chat import GroupChat
from status import Status
from web_application import WebApplication
from cryptography.fernet import Fernet


def test_integration():
	# Create a user
	user = User('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.password == 'password'

	# Create a profile for the user
	profile = Profile(user)
	profile.set_profile_picture('picture.jpg')
	profile.set_status_message('Hello, world!')
	profile.manage_privacy_settings({'last_seen': 'public'})
	assert profile.user == user
	assert profile.profile_picture == 'picture.jpg'
	assert profile.status_message == 'Hello, world!'
	assert profile.privacy_settings == {'last_seen': 'public'}

	# Create a contact for the user
	contact = Contact()
	contact.block_contact('spam@example.com')
	assert 'spam@example.com' in contact.blocked_contacts

	# Create a message from the user
	key = Fernet.generate_key()
	message = Message(user.email, 'friend@example.com', 'Hello, friend!')
	message.encrypt_message(key)
	assert message.sender == user.email
	assert message.receiver == 'friend@example.com'
	assert message.content != 'Hello, friend!'

	# Decrypt the message
	message.decrypt_message(key)
	assert message.content == 'Hello, friend!'

	# Create a group chat with the user and a friend
	group_chat = GroupChat('Test Group')
	group_chat.create_group_chat('Test Group', 'group.jpg', [user.email, 'friend@example.com'], [user.email])
	assert group_chat.name == 'Test Group'
	assert group_chat.picture == 'group.jpg'
	assert user.email in group_chat.participants
	assert 'friend@example.com' in group_chat.participants
	assert user.email in group_chat.admins

	# Create a status for the user
	status = Status(user, 'Hello, world!', 'public')
	assert status.user == user
	assert status.content == 'Hello, world!'
	assert status.visibility == 'public'

	# Create a web application and set the current user
	web_application = WebApplication()
	web_application.set_current_user(user)
	assert web_application.get_current_user() == user

