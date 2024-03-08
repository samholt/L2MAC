class Folder:
	def __init__(self, name):
		self.name = name
		self.files = []
		self.folders = []
		self.permissions = []

	def add_file(self, file):
		self.files.append(file)

	def remove_file(self, file):
		self.files.remove(file)

	def add_folder(self, folder):
		self.folders.append(folder)

	def remove_folder(self, folder):
		self.folders.remove(folder)

	def add_permission(self, permission):
		self.permissions.append(permission)

	def remove_permission(self, permission):
		self.permissions.remove(permission)
