from dataclasses import dataclass, field
import uuid

@dataclass
class Message:
	id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
	sender_id: str
	content: str

	def to_dict(self):
		return {'id': self.id, 'sender_id': self.sender_id, 'content': self.content}

@dataclass
class Chat:
	id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
	name: str
	messages: list = field(default_factory=list)

	def send_message(self, sender_id, content):
		message = Message(sender_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.to_dict() for message in self.messages]}
