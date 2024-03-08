class File:
	id_counter = 1
	def __init__(self, name, content, owner):
		self.id = File.id_counter
		File.id_counter += 1
		self.name = name
		self.content = content
		self.owner = owner
		self.permissions = {}

	def view(self):
		return self.content

	def edit(self, content):
		self.content = content

	def share(self, user, permission):
		self.permissions[user.username] = permission

	def download(self):
		return self.content

	def check_permission(self, user, permission):
		return self.permissions.get(user.username, None) == permission
