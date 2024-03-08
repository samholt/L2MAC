import pytest
from user import User

def test_user():
	user = User('test@test.com', 'password')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert user.profile_picture == None
	assert user.status_message == None
	assert user.privacy_settings == None
	assert user.contacts == {}
	assert user.blocked_contacts == {}
	assert user.groups == {}
	assert user.status == None

	user.sign_up('new@test.com', 'new_password')
	assert user.email == 'new@test.com'
	assert user.password == 'new_password'

	assert user.recover_password('new@test.com') == 'new_password'

	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'

	user.set_status_message('Hello, world!')
	assert user.status_message == 'Hello, world!'

	user.set_privacy_settings('private')
	assert user.privacy_settings == 'private'

	user.contacts = {'contact1': 'Contact 1'}
	user.block_contact('contact1')
	assert user.contacts == {}
	assert user.blocked_contacts == {'contact1': 'Contact 1'}

	user.unblock_contact('contact1')
	assert user.contacts == {'contact1': 'Contact 1'}
	assert user.blocked_contacts == {}

	user.create_group('Group 1')
	assert user.groups == {'Group 1': []}

	user.edit_group('Group 1', 'Group 2')
	assert user.groups == {'Group 2': []}

	user.manage_group('Group 2', 'add', 'contact1')
	assert user.groups == {'Group 2': ['contact1']}

	user.manage_group('Group 2', 'remove', 'contact1')
	assert user.groups == {'Group 2': []}

	message = user.send_message('contact1', 'Hello, contact1')
	assert message == {'recipient': 'contact1', 'message': 'Hello, contact1'}

	received_message = user.receive_message('contact1', 'Hello, user')
	assert received_message == {'sender': 'contact1', 'message': 'Hello, user'}

	read_message = user.read_message('Hello, user')
	assert read_message == 'Hello, user'

	encrypted_message = user.encrypt_message('Hello, user')
	assert encrypted_message == 'Hello, user'

	decrypted_message = user.decrypt_message('Hello, user')
	assert decrypted_message == 'Hello, user'

	image = user.share_image('contact1', 'image.jpg')
	assert image == {'recipient': 'contact1', 'image': 'image.jpg'}

	emoji = user.send_emoji('contact1', ':)')
	assert emoji == {'recipient': 'contact1', 'emoji': ':)'}

	user.create_group_chat('Group 3')
	assert 'Group 3' in user.groups

	user.add_participant('Group 3', 'contact1')
	assert 'contact1' in user.groups['Group 3']

	user.remove_participant('Group 3', 'contact1')
	assert 'contact1' not in user.groups['Group 3']

	admin = user.assign_admin_role('Group 3', 'contact1')
	assert admin == {'group': 'Group 3', 'admin': 'contact1'}

	removed_admin = user.remove_admin_role('Group 3', 'contact1')
	assert removed_admin == {'group': 'Group 3', 'admin': 'contact1'}

	user.post_status('Hello, world!')
	assert user.status == 'Hello, world!'

	status = user.view_status()
	assert status == 'Hello, world!'

	queued_message = user.queue_message('contact1', 'Hello, contact1')
	assert queued_message == {'recipient': 'contact1', 'message': 'Hello, contact1'}

	assert user.display_online_status() == 'online'
