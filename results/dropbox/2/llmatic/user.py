class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.files = []
		self.folders = []

	def upload_file(self, file):
		file.id = len(self.files)
		file.permissions = [(self.username, 'rw')]
		self.files.append(file)
		return file.id

	def view_file(self, file_id):
		for file in self.files:
			if file.id == file_id:
				for permission in file.permissions:
					if permission[0] == self.username and 'r' in permission[1]:
						return file.content
					elif permission[0] != self.username and 'r' in permission[1]:
						return file.content
		return None

	def search_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				return file.id
		return None

	def share_file(self, file_id, user, permission):
		for file in self.files:
			if file.id == file_id:
				file.permissions.append((user.username, permission))
				user.files.append(file)

	def download_file(self, file_id):
		for file in self.files:
			if file.id == file_id:
				for permission in file.permissions:
					if permission[0] == self.username and 'r' in permission[1]:
						return file.content
					elif permission[0] != self.username and 'r' in permission[1]:
						return file.content
		return None
