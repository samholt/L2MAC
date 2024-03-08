class File:
	def __init__(self, name, type, size, content):
		self.name = name
		self.type = type
		self.size = size
		self.content = content
		self.versions = [content]

	def add_version(self, new_content):
		self.content = new_content
		self.versions.append(new_content)

	def restore_version(self, version_number):
		if version_number < len(self.versions):
			self.content = self.versions[version_number]


class Folder:
	def __init__(self, name):
		self.name = name
		self.files = {}

	def add_file(self, file):
		self.files[file.name] = file

	def remove_file(self, file_name):
		if file_name in self.files:
			del self.files[file_name]

	def move_file(self, file_name, target_folder):
		if file_name in self.files:
			file = self.files[file_name]
			del self.files[file_name]
			target_folder.add_file(file)

	def rename_file(self, old_name, new_name):
		if old_name in self.files:
			file = self.files[old_name]
			file.name = new_name
			self.files[new_name] = file
			del self.files[old_name]


class FileDatabase:
	def __init__(self):
		self.files = {}
		self.folders = {}

	def upload(self, file, folder_name=None):
		if folder_name:
			if folder_name in self.folders:
				self.folders[folder_name].add_file(file)
			else:
				new_folder = Folder(folder_name)
				new_folder.add_file(file)
				self.folders[folder_name] = new_folder
		else:
			self.files[file.name] = file

	def download(self, file_name, folder_name=None):
		if folder_name:
			if folder_name in self.folders:
				return self.folders[folder_name].files.get(file_name, None)
		return self.files.get(file_name, None)

	def create_folder(self, folder):
		self.folders[folder.name] = folder

	def move_file(self, file_name, folder_name):
		if file_name in self.files:
			file = self.files[file_name]
			del self.files[file_name]
			self.folders[folder_name].add_file(file)
