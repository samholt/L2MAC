from dataclasses import dataclass

@dataclass
class Message:
	def __init__(self, sender, recipient, content, content_type):
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.content_type = content_type  # 'text', 'image', 'emoji', 'gif', 'sticker'

	def get_content(self):
		return self.content

	def get_content_type(self):
		return self.content_type
