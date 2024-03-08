class FileManager:
	def __init__(self):
		self.files = {}

	def upload(self, data):
		file = data.get('file')
		if not file:
			return {'status': 'error', 'message': 'No file provided'}
		self.files[file['name']] = file['content']
		return {'status': 'success', 'message': 'File uploaded successfully'}

	def download(self, data):
		file_name = data.get('file_name')
		if not file_name:
			return {'status': 'error', 'message': 'No file name provided'}
		if file_name not in self.files:
			return {'status': 'error', 'message': 'File not found'}
		return {'status': 'success', 'message': 'File downloaded successfully', 'file': {'name': file_name, 'content': self.files[file_name]}}
