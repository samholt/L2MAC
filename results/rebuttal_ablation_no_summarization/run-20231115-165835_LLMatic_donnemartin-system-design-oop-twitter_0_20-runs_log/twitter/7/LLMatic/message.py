from dataclasses import dataclass
from typing import Dict, List

# Mock database
messages_db: Dict[int, 'Message'] = {}
blocked_users: Dict[str, List[str]] = {}

@dataclass
class Message:
	text: str
	sender: str
	receiver: str


def send_message(text: str, sender: str, receiver: str) -> Message:
	"""Send a message from one user to another."""
	# Check if the sender is blocked by the receiver
	if receiver in blocked_users and sender in blocked_users[receiver]:
		return None
	message = Message(text, sender, receiver)
	message_id = len(messages_db) + 1
	messages_db[message_id] = message
	return message


def block_user(username: str, user_to_block: str) -> bool:
	"""Block a user from sending messages."""
	if username not in blocked_users:
		blocked_users[username] = []
	blocked_users[username].append(user_to_block)
	return True


def unblock_user(username: str, user_to_unblock: str) -> bool:
	"""Unblock a user from sending messages."""
	if username in blocked_users and user_to_unblock in blocked_users[username]:
		blocked_users[username].remove(user_to_unblock)
		return True
	return False
