class File:
	def __init__(self, name, file_type, size, content):
		self.name = name
		self.file_type = file_type
		self.size = size
		self.content = content
		self.versions = [content]

	def add_version(self, content):
		self.versions.append(content)

	def get_version(self, version_number):
		return self.versions[version_number]

	def rename(self, new_name):
		self.name = new_name

	def move(self, new_folder):
		self.folder = new_folder


class Folder:
	def __init__(self, name):
		self.name = name
		self.files = []
		self.folders = []

	def add_file(self, file):
		self.files.append(file)

	def add_folder(self, folder):
		self.folders.append(folder)

	def rename(self, new_name):
		self.name = new_name

	def delete_file(self, file_name):
		for file in self.files:
			if file.name == file_name:
				self.files.remove(file)
				return 'File deleted successfully'
		return 'File not found'

	def delete_folder(self, folder_name):
		for folder in self.folders:
			if folder.name == folder_name:
				self.folders.remove(folder)
				return 'Folder deleted successfully'
		return 'Folder not found'

mock_db_files = {}

from user import mock_db

def upload(file, email):
	if email in mock_db:
		user = mock_db[email]
		if user.storage_remaining >= file.size:
			user.storage_used += file.size
			user.storage_remaining -= file.size
			if email in mock_db_files:
				for stored_file in mock_db_files[email]:
					if stored_file.name == file.name:
						if stored_file.content != file.content:
							stored_file.add_version(file.content)
							return {'message': 'File version uploaded successfully', 'status': 200}
						else:
							return {'message': 'File already exists', 'status': 400}
				mock_db_files[email].append(file)
			else:
				mock_db_files[email] = [file]
			return {'message': 'File uploaded successfully', 'status': 200}
		else:
			return {'message': 'Not enough storage', 'status': 400}
	else:
		return {'message': 'User not found', 'status': 400}

def download(file_name, email, version_number=0):
	if email in mock_db and email in mock_db_files:
		for file in mock_db_files[email]:
			if file.name == file_name:
				return {'file': file.get_version(version_number), 'status': 200}
		return {'message': 'File not found', 'status': 400}
	else:
		return {'message': 'User not found', 'status': 400}
