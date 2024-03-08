from dataclasses import dataclass
from user import User, users_db

# Mock database
messages_db = {}

@dataclass
class Message:
	content: str
	sender: User
	receiver: User


def send_message(sender_username: str, receiver_username: str, content: str) -> str:
	if sender_username in users_db and receiver_username in users_db:
		sender = users_db[sender_username]
		receiver = users_db[receiver_username]
		if receiver_username not in sender.blocked_users:
			message = Message(content, sender, receiver)
			messages_db[len(messages_db) + 1] = message
			return 'Message sent successfully'
		else:
			return 'User is blocked'
	else:
		return 'User not found'


def block_user(username: str, user_to_block: str) -> str:
	if username in users_db and user_to_block in users_db:
		user = users_db[username]
		if user_to_block not in user.blocked_users:
			user.blocked_users.append(user_to_block)
			users_db[username] = user
			return 'User blocked successfully'
		else:
			return 'User already blocked'
	else:
		return 'User not found'


def unblock_user(username: str, user_to_unblock: str) -> str:
	if username in users_db and user_to_unblock in users_db:
		user = users_db[username]
		if user_to_unblock in user.blocked_users:
			user.blocked_users.remove(user_to_unblock)
			users_db[username] = user
			return 'User unblocked successfully'
		else:
			return 'User not blocked'
	else:
		return 'User not found'
