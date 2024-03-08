from models.file import File
import os
import zipfile


class FileService:
	def __init__(self):
		self.files = {}

	def upload_file(self, user, file):
		if file['size'] > 1000:
			return 'File size exceeds limit'
		if file['type'] not in ['txt', 'pdf', 'jpg', 'png']:
			return 'File type not allowed'
		file_id = len(self.files) + 1
		new_file = File(file_id, file['name'], file['type'], file['size'], 1, user.get_id())
		self.files[file_id] = new_file
		user.set_storage_used(user.get_storage_used() + file['size'])
		return 'File uploaded successfully'

	def get_file(self, file_id):
		return self.files.get(file_id, 'File not found')

	def download_file(self, file_id):
		file = self.get_file(file_id)
		if file == 'File not found':
			return 'File not found'
		return f'Download link: /download/{file_id}'

	def download_folder_as_zip(self, folder_path):
		zipf = zipfile.ZipFile('Folder.zip', 'w', zipfile.ZIP_DEFLATED)
		for root, dirs, files in os.walk(folder_path):
			for file in files:
				zipf.write(os.path.join(root, file))
		zipf.close()
		return 'Download link: /download/Folder.zip'
