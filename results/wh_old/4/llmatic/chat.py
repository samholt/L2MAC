from dataclasses import dataclass, field
from message import Message

@dataclass
class Chat:
	id: str
	user_ids: list
	messages: list = field(default_factory=list)

	def add_message(self, message: Message):
		self.messages.append(message)

	def get_chat_history(self):
		return self.messages

	def mark_as_read(self, message_id: str):
		for message in self.messages:
			if message.id == message_id:
				message.status = 'read'
				break

