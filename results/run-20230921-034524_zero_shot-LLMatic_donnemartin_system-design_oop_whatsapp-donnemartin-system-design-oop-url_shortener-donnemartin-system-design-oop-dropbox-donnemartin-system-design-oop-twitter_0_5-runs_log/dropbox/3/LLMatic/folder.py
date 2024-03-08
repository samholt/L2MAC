class Folder:
	def __init__(self, name, owner):
		self.name = name
		self.owner = owner
		self.files = []
		self.permissions = {}

	def create_folder(self, name):
		new_folder = Folder(name, self.owner)
		self.files.append(new_folder)
		return new_folder

	def delete_folder(self, name):
		for folder in self.files:
			if folder.name == name:
				self.files.remove(folder)
				return True
		return False

	def add_file(self, file):
		self.files.append(file)

	def remove_file(self, file):
		if file in self.files:
			self.files.remove(file)
			return True
		return False

	def grant_permission(self, user, permission):
		self.permissions[user.username] = permission

	def revoke_permission(self, user):
		if user.username in self.permissions:
			del self.permissions[user.username]
			return True
		return False

	def check_permission(self, user):
		return self.permissions.get(user.username, None)
