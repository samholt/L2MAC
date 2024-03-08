class File:
	def __init__(self, name, file_type, size, content):
		self.name = name
		self.file_type = file_type
		self.size = size
		self.content = content

mock_db = {}

ALLOWED_FILE_TYPES = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
MAX_FILE_SIZE = 1000000

def upload_file(file):
	if file.file_type not in ALLOWED_FILE_TYPES:
		return 'File type not allowed'
	if file.size > MAX_FILE_SIZE:
		return 'File size exceeds limit'
	mock_db[file.name] = file
	return 'File uploaded successfully'

def download_file(file_name):
	if file_name in mock_db:
		return mock_db[file_name].content
	else:
		return None
