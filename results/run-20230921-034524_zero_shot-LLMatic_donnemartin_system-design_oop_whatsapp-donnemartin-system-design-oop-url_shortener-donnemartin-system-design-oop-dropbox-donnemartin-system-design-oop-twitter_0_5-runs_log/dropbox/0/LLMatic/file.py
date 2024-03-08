class File:
	def __init__(self, file_id, file_name, file_size, file_content):
		self.file_id = file_id
		self.file_name = file_name
		self.file_size = file_size
		self.file_content = file_content

	def upload(self, file_content):
		# Simulate file upload logic
		self.file_content = file_content
		print(f"File {self.file_name} uploaded with content: {self.file_content}")

	def download(self):
		# Simulate file download logic
		print(f"File {self.file_name} downloaded with content: {self.file_content}")
		return self.file_content

	def view(self):
		# Simulate file view logic
		print(f"File {self.file_name} viewed with content: {self.file_content}")
		return self.file_content

	def delete(self):
		# Simulate file delete logic
		self.file_content = None
		print(f"File {self.file_name} deleted")
