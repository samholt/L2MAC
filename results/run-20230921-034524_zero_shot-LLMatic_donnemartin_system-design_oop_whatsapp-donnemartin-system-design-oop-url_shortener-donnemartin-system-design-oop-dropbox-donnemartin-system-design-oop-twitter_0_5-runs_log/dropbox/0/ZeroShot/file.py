class File:
	def __init__(self, file_id, user_id, data):
		self.file_id = file_id
		self.user_id = user_id
		self.data = data

	def read(self):
		return self.data

	def write(self, data):
		self.data = data

	def delete(self):
		self.data = None
