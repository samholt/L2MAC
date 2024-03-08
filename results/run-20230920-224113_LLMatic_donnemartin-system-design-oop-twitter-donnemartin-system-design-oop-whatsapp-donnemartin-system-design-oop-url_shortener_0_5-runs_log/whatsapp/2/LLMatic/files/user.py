from dataclasses import dataclass, field
from message import Message
from chat import Chat
from group_chat import GroupChat

@dataclass
class User:
	id: str
	name: str
	chats: dict = field(default_factory=dict)

	def send_message(self, chat_id, message):
		chat = self.chats[chat_id]
		chat.add_message(message)

	def receive_message(self, chat_id, message):
		chat = self.chats[chat_id]
		chat.add_message(message)

	def create_group_chat(self, user_ids):
		group_chat = GroupChat(user_ids)
		self.chats[group_chat.id] = group_chat

	def view_chat_history(self, chat_id):
		chat = self.chats[chat_id]
		return chat.get_chat_history()

