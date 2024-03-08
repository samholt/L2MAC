class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.files = []

	def upload_file(self, file):
		self.files.append(file)

	def view_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				return file
		return None

	def search_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				return file
		return None

	def share_file(self, file_name, user):
		for file in self.files:
			if file.name == file_name:
				user.files.append(file)
				return True
		return False

	def download_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				return file
		return None
