from cloudsafe.app.models import File, Folder


class FileService:
	def __init__(self):
		self.files = {}
		self.folders = {}

	def upload_file(self, id, name, user_id, folder_id=None):
		file = File(id, name, user_id, folder_id)
		self.files[id] = file
		return 'File uploaded successfully'

	def download_file(self, id):
		file = self.files.get(id)
		if file:
			return 'File downloaded successfully'
		return 'File not found'

	def move_file(self, id, new_folder_id):
		file = self.files.get(id)
		if file:
			file.folder_id = new_folder_id
			return 'File moved successfully'
		return 'File not found'

	def rename_file(self, id, new_name):
		file = self.files.get(id)
		if file:
			file.name = new_name
			return 'File renamed successfully'
		return 'File not found'

	def delete_file(self, id):
		if id in self.files:
			del self.files[id]
			return 'File deleted successfully'
		return 'File not found'

	def create_folder(self, id, name, user_id, parent_folder_id=None):
		folder = Folder(id, name, user_id, parent_folder_id)
		self.folders[id] = folder
		return 'Folder created successfully'

	def rename_folder(self, id, new_name):
		folder = self.folders.get(id)
		if folder:
			folder.name = new_name
			return 'Folder renamed successfully'
		return 'Folder not found'

	def move_folder(self, id, new_parent_folder_id):
		folder = self.folders.get(id)
		if folder:
			folder.parent_folder_id = new_parent_folder_id
			return 'Folder moved successfully'
		return 'Folder not found'

	def delete_folder(self, id):
		if id in self.folders:
			del self.folders[id]
			return 'Folder deleted successfully'
		return 'Folder not found'

