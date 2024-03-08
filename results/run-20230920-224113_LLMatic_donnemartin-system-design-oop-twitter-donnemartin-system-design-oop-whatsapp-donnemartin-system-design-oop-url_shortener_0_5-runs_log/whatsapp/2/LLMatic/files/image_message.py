from message import Message


class ImageMessage(Message):
	def __init__(self, id, sender_id, receiver_id, content, image_data, status='sent'):
		super().__init__(id, sender_id, receiver_id, content, status)
		self.image_data = image_data

	def set_image_data(self, image_data):
		self.image_data = image_data

	def get_image_data(self):
		return self.image_data

