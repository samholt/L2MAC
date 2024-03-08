from models.file import File


class FileService:
	def __init__(self):
		self.files = {}
		self.folders = {}
		self.shared_folders = {}

	def upload_file(self, file):
		self.files[file.name] = file

	def download_file(self, file_name):
		return self.files.get(file_name, None)

	def create_folder(self, folder_name):
		self.folders[folder_name] = []

	def share_folder(self, folder_name, user_email, permissions):
		if folder_name in self.folders:
			if folder_name not in self.shared_folders:
				self.shared_folders[folder_name] = []
			self.shared_folders[folder_name].append((user_email, permissions))

	def rename_file(self, old_name, new_name):
		if old_name in self.files:
			self.files[new_name] = self.files.pop(old_name)

	def move_file(self, file_name, folder_name):
		if file_name in self.files and folder_name in self.folders:
			self.folders[folder_name].append(self.files.pop(file_name))

	def delete_file(self, file_name):
		if file_name in self.files:
			del self.files[file_name]

	def restore_file(self, file_name, version):
		if file_name in self.files:
			file = self.files[file_name]
			if version in file.previous_versions:
				file.version = version
				file.previous_versions.remove(version)
