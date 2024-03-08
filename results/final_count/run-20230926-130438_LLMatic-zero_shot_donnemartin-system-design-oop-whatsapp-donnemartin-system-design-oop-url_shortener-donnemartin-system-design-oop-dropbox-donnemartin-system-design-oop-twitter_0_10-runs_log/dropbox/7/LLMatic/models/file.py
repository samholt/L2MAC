class File:
	def __init__(self, id, name, type, size, version, owner):
		self.id = id
		self.name = name
		self.type = type
		self.size = size
		self.version = version
		self.owner = owner

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_type(self, type):
		self.type = type

	def get_type(self):
		return self.type

	def set_size(self, size):
		self.size = size

	def get_size(self):
		return self.size

	def set_version(self, version):
		self.version = version

	def get_version(self):
		return self.version

	def set_owner(self, owner):
		self.owner = owner

	def get_owner(self):
		return self.owner
