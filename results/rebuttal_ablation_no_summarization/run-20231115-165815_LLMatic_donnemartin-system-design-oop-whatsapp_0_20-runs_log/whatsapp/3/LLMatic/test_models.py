from models.user import User
from models.group import Group
from models.message import Message


def test_user_model():
	user = User('test@test.com', 'password', 'profile_picture', 'status_message', 'privacy_settings')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert user.profile_picture == 'profile_picture'
	assert user.status_message == 'status_message'
	assert user.privacy_settings == 'privacy_settings'


def test_group_model():
	group = Group('group_name', 'group_picture', ['participant1', 'participant2'], ['admin1', 'admin2'])
	assert group.name == 'group_name'
	assert group.picture == 'group_picture'
	assert group.participants == ['participant1', 'participant2']
	assert group.admin_roles == ['admin1', 'admin2']


def test_message_model():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello, World!', True, False, 'image')
	assert message.sender == 'sender@test.com'
	assert message.receiver == 'receiver@test.com'
	assert message.content == 'Hello, World!'
	assert message.read_receipt == True
	assert message.encryption == False
	assert message.image == 'image'
