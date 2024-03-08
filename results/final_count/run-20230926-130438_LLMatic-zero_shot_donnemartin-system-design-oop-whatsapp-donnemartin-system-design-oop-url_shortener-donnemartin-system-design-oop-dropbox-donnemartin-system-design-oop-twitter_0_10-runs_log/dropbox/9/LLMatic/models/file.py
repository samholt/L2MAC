class File:
	def __init__(self, id, content, size, upload_date, owner, versions):
		self.id = id
		self.content = content
		self.size = size
		self.upload_date = upload_date
		self.owner = owner
		self.versions = versions
		self.shared_with = []
