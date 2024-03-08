from datetime import datetime


class File:
	def __init__(self, name, size, type, upload_date, version, parent_folder):
		self.name = name
		self.size = size
		self.type = type
		self.upload_date = upload_date if upload_date else datetime.now()
		self.version = version
		self.parent_folder = parent_folder

	def upload(self, file):
		# Implement file upload logic here
		pass

	def download(self):
		# Implement file download logic here
		pass

	def rename(self, new_name):
		self.name = new_name

	def move(self, new_folder):
		self.parent_folder = new_folder

	def delete(self):
		# Implement file deletion logic here
		pass

	def versioning(self, new_version):
		self.version = new_version
