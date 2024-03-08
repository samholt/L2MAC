from models.message import Message
import base64

class ImageMessage(Message):
	def __init__(self, sender, chat, image_path):
		super().__init__(sender, chat, '')
		self.image_path = image_path
		self.image_data = None

	def read_image(self):
		try:
			with open(self.image_path, 'rb') as image_file:
				self.image_data = base64.b64encode(image_file.read()).decode()
				self.content = self.image_data
		except FileNotFoundError:
			print(f'Image file {self.image_path} not found.')

	def write_image(self, output_path):
		with open(output_path, 'wb') as image_file:
			image_file.write(base64.b64decode(self.image_data))

	def encrypt_content(self):
		self.read_image()
		if self.image_data is not None:
			self.content = base64.b64encode(self.image_data.encode()).decode()
			self.image_data = self.content

	def decrypt_content(self, output_path):
		if self.content is not None:
			self.content = base64.b64decode(self.content).decode()
			self.image_data = self.content
			self.write_image(output_path)
