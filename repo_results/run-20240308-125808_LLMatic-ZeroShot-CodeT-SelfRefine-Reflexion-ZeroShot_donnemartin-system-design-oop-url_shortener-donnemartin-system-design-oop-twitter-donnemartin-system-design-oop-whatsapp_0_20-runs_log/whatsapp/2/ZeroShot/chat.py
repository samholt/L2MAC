from dataclasses import dataclass, field

@dataclass
class Chat:
	id: str
	name: str
	user_ids: list
	messages: list = field(default_factory=list)

	def send_message(self, user_id, content):
		self.messages.append({'user_id': user_id, 'content': content})

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'user_ids': self.user_ids,
			'messages': self.messages
		}
