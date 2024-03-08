from user import User


class Message:
	def __init__(self, sender: User, content: str):
		self.sender = sender
		self.content = content

	def set_text(self, text: str):
		self.content = text

	def set_image(self, image: str):
		self.content = image

	def set_emoji(self, emoji: str):
		self.content = emoji
