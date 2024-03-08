class SharedFile:
	def __init__(self, file, owner, shared_with):
		self.file = file
		self.owner = owner
		self.shared_with = shared_with

	def share(self, user):
		if user.username not in self.shared_with:
			self.shared_with.append(user.username)

	def unshare(self, user):
		if user.username in self.shared_with:
			self.shared_with.remove(user.username)

	def edit(self, content):
		if self.owner == user:
			self.file.content = content
		else:
			print('Only the owner can edit the file.')
