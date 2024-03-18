class MockDB:
	def __init__(self):
		self.data = {}

	def add(self, key, value):
		self.data[key] = value

	def update(self, key, value):
		if key in self.data:
			self.data[key] = value

	def delete(self, key):
		if key in self.data:
			del self.data[key]

	def retrieve(self, key):
		return self.data.get(key, None)
