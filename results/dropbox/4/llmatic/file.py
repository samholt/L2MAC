class File:
	def __init__(self, name, size, type, content):
		self.name = name
		self.size = size
		self.type = type
		self.content = content

	def read_content(self):
		return self.content

	def write_content(self, content):
		self.content = content
