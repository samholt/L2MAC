class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.files = []
		self.folders = []
		self.permissions = {}

	def upload_file(self, file):
		self.files.append(file)

	def view_file(self, file_id):
		for file in self.files:
			if file.id == file_id:
				return file
		return None

	def search_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				return file
		return None

	def share_file(self, file_id, user):
		file = self.view_file(file_id)
		if file:
			user.files.append(file)

	def download_file(self, file_id):
		file = self.view_file(file_id)
		if file:
			return file.content
		return None

	def edit_file(self, file_id, content):
		file = self.view_file(file_id)
		if file and self.permissions.get(file_id, False):
			file.content = content
			return True
		return False

	def grant_permission(self, file_id):
		self.permissions[file_id] = True

	def revoke_permission(self, file_id):
		self.permissions[file_id] = False
