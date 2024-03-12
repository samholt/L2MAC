from dataclasses import dataclass

@dataclass
class Chat:
	id: str
	members: list
	messages: list = None

	def add_member(self, member):
		self.members.append(member)

	def remove_member(self, member):
		if member in self.members:
			self.members.remove(member)

	def send_message(self, message):
		if self.messages is None:
			self.messages = []
		self.messages.append(message)
