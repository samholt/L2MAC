class Sharing:
	def __init__(self, file_id, user_id, permission_level):
		self.file_id = file_id
		self.user_id = user_id
		self.permission_level = permission_level
		self.shared_files = {}

	def share(self, user_id, permission_level):
		if self.file_id not in self.shared_files:
			self.shared_files[self.file_id] = {}
		self.shared_files[self.file_id][user_id] = permission_level

	def unshare(self, user_id):
		if self.file_id in self.shared_files and user_id in self.shared_files[self.file_id]:
			del self.shared_files[self.file_id][user_id]
