from dataclasses import dataclass, field
from typing import List


@dataclass
class Message:
	text: str
	sender: str
	recipient: str
	blocked_users: List[str] = field(default_factory=list)

	def send_message(self):
		if self.recipient in self.blocked_users:
			return 'User is blocked'
		return 'Message sent'

	def delete_message(self):
		return 'Message deleted'

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)
		return 'User blocked'

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
		return 'User unblocked'
