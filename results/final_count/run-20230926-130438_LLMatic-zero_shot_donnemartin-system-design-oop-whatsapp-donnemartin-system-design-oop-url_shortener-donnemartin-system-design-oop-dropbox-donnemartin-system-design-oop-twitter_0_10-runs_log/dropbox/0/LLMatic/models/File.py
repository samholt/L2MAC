class File:
	def __init__(self, id, name, type, size, path, user, tags):
		self.id = id
		self.name = name
		self.type = type
		self.size = size
		self.path = path
		self.user = user
		self.tags = tags

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'type': self.type,
			'size': self.size,
			'path': self.path,
			'user': self.user,
			'tags': self.tags
		}
