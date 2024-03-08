from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Message:
	sender: str
	recipient: str
	content: str
	read_receipt: bool
	encrypted: bool
	queued: bool = False
	group_chat: str = None


messages_db = {}
group_chats_db = {}


def send_message(sender: str, recipient: str, content: str, group_chat: str = None):
	message = Message(sender, recipient, content, False, False, False, group_chat)
	messages_db[(sender, recipient)] = message


def queue_message(sender: str, recipient: str):
	message = messages_db.get((sender, recipient))
	if message:
		message.queued = True


def read_message(sender: str, recipient: str):
	message = messages_db.get((sender, recipient))
	if message:
		message.read_receipt = True
		return message


def update_read_receipt(sender: str, recipient: str):
	message = messages_db.get((sender, recipient))
	if message:
		message.read_receipt = True


def encrypt_message(sender: str, recipient: str):
	message = messages_db.get((sender, recipient))
	if message:
		message.content = 'Encrypted: ' + message.content
		message.encrypted = True


def share_image(sender: str, recipient: str, image_content: str):
	message = Message(sender, recipient, image_content, False, True, False, None)
	messages_db[(sender, recipient)] = message


def create_group_chat(name: str, participants: List[str]):
	group_chats_db[name] = participants


def add_participant(group_chat: str, participant: str):
	if group_chat in group_chats_db:
		group_chats_db[group_chat].append(participant)


def remove_participant(group_chat: str, participant: str):
	if group_chat in group_chats_db:
		group_chats_db[group_chat].remove(participant)


def set_admin(group_chat: str, admin: str):
	if group_chat in group_chats_db and admin in group_chats_db[group_chat]:
		group_chats_db[group_chat] = [admin] + [user for user in group_chats_db[group_chat] if user != admin]
