from database import Database


class File:
	def __init__(self, file_name, file_size, file_type, file_content):
		self.file_name = file_name
		self.file_size = file_size
		self.file_type = file_type
		self.file_content = file_content
		self.permissions = []
		self.versions = []
		self.db = Database('file_storage.db')

	def upload(self):
		# Handle large file upload
		if self.file_size > 1024 * 1024 * 1024:
			self.split_file()
		query = 'INSERT INTO files (file_name, file_size, file_type, file_content) VALUES (?, ?, ?, ?)'
		params = (self.file_name, self.file_size, self.file_type, self.file_content)
		self.db.execute_query(query, params)
		self.db.commit_transaction()

	def download(self):
		# Handle large file download
		if self.file_size > 1024 * 1024 * 1024:
			self.merge_file()
		# Download logic goes here
		pass

	def view(self):
		# View logic goes here
		pass

	def delete(self):
		# Delete logic goes here
		pass

	def get_metadata(self):
		# Logic to get file's metadata goes here
		return {'file_name': self.file_name, 'file_size': self.file_size, 'file_type': self.file_type}

	def add_permission(self, user):
		# Logic to add user to permissions list
		self.permissions.append(user)

	def remove_permission(self, user):
		# Logic to remove user from permissions list
		self.permissions.remove(user)

	def get_permissions(self):
		# Logic to get permissions list
		return self.permissions

	def add_version(self, version):
		# Logic to add version to versions list
		self.versions.append(version)

	def get_versions(self):
		# Logic to get versions list
		return self.versions

	def split_file(self):
		# Logic to split large file into smaller chunks
		pass

	def merge_file(self):
		# Logic to merge file chunks into a single large file
		pass

