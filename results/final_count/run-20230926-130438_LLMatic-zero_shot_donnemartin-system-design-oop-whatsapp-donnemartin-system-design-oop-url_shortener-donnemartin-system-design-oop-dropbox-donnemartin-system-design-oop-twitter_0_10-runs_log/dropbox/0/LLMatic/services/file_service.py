from models.File import File


class FileService:
	def __init__(self):
		self.files = {}

	def get_files(self):
		return 'Get Files'

	def upload_file(self, file, user):
		file_id = len(self.files) + 1
		new_file = File(file_id, file['name'], file['type'], file['size'], file['path'], user, [])
		self.files[file_id] = new_file
		return new_file.to_dict()

	def download_file(self, file_id):
		if file_id in self.files:
			return self.files[file_id].to_dict()
		else:
			return 'File not found'

	def create_folder(self, folder_name, user):
		folder_id = len(self.files) + 1
		new_folder = File(folder_id, folder_name, 'folder', 0, '', user, [])
		self.files[folder_id] = new_folder
		return new_folder.to_dict()

	def rename_file(self, file_id, new_name):
		if file_id in self.files:
			self.files[file_id].name = new_name
			return self.files[file_id].to_dict()
		else:
			return 'File not found'

	def move_file(self, file_id, new_path):
		if file_id in self.files:
			self.files[file_id].path = new_path
			return self.files[file_id].to_dict()
		else:
			return 'File not found'

	def delete_file(self, file_id):
		if file_id in self.files:
			del self.files[file_id]
			return 'File deleted'
		else:
			return 'File not found'

	def generate_shareable_link(self, file_id):
		if file_id in self.files:
			return 'http://localhost:5000/download/' + str(file_id)
		else:
			return 'File not found'
