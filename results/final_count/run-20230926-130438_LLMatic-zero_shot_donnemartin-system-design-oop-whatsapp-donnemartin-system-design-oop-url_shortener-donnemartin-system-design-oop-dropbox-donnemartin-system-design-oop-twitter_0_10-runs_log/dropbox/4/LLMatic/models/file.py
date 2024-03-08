class File:
	def __init__(self, name, file_type, size, upload_date, folder=None, version=1, previous_versions=None):
		self.name = name
		self.file_type = file_type
		self.size = size
		self.upload_date = upload_date
		self.folder = folder
		self.version = version
		self.previous_versions = previous_versions if previous_versions else []
