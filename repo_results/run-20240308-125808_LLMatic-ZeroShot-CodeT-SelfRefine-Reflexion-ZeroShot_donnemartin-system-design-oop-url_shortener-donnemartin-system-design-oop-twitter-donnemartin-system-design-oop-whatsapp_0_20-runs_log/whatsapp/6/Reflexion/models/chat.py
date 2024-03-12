from dataclasses import dataclass

@dataclass
class Chat:
	id: str
	name: str
	members: list = None
	messages: list = None

	def add_member(self, member):
		if self.members is None:
			self.members = []
		self.members.append(member)

	def remove_member(self, member):
		if self.members is not None and member in self.members:
			self.members.remove(member)

	def add_message(self, message):
		if self.messages is None:
			self.messages = []
		self.messages.append(message)
