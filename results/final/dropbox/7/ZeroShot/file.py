class File:
	def __init__(self, name, type, size, content):
		self.name = name
		self.type = type
		self.size = size
		self.content = content

	def to_dict(self):
		return {
			'name': self.name,
			'type': self.type,
			'size': self.size,
			'content': self.content
		}
