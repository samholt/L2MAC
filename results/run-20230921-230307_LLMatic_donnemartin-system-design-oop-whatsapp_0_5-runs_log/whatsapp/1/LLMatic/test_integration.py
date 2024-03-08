from user import User
from chat import Chat
from group import Group
from status import Status

def test_integration():
	# Create instances of User
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')

	# Create an instance of Chat
	chat = Chat(user1, user2)

	# User1 sends a message to User2
	message_text = 'Hello, User2!'
	chat.send_message(user1, user2, message_text)

	# User2 receives the message
	chat.receive_message(user1, user2, message_text)

	# Check read receipts
	assert chat.display_read_receipts()[(user1, user2, message_text)] == True

	# Create an instance of Group
	group = Group('Group1', user1)

	# User1 adds User2 to the group
	group.add_participant(user2)

	# Check if User2 is in the group
	assert user2 in group.participants

	# Create an instance of Status
	status = Status(user1, 'image_path', 'Feeling happy!')

	# Check if the status message is correct
	assert status.message == 'Feeling happy!'
