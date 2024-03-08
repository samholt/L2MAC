class File:
	def __init__(self, name, size, content):
		self.id = None
		self.name = name
		self.size = size
		self.content = content
		self.permissions = []

	def add_permission(self, permission):
		if permission not in self.permissions:
			self.permissions.append(permission)

	def remove_permission(self, permission):
		if permission in self.permissions:
			self.permissions.remove(permission)
