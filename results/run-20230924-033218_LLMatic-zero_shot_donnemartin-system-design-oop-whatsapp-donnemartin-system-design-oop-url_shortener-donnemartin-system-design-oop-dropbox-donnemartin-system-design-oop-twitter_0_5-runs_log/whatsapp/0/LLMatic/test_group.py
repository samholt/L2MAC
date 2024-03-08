import pytest
from group import Group
from user import User


def test_group():
	group = Group('Test Group', 'test.jpg', [], [], [])
	user = User('test@test.com', 'password')

	group.create('New Group', 'new.jpg')
	assert group.name == 'New Group'
	assert group.picture == 'new.jpg'

	group.add_participant(user)
	assert user in group.participants

	group.remove_participant(user)
	assert user not in group.participants

	group.assign_admin_role(user)
	assert user in group.admins

	group.remove_admin_role(user)
	assert user not in group.admins

	group.send_message('Hello')
	assert 'Hello' in group.messages

	group.receive_message('Hi')
	assert 'Hi' in group.messages

	assert group.read_message('Hello')

	group.share_image('image.jpg')
	assert 'image.jpg' in group.messages

	group.send_emoji('emoji')
	assert 'emoji' in group.messages
