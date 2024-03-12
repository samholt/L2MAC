class MockDB:
	def __init__(self):
		self.db = {}

	def add(self, key, value):
		self.db[key] = value

	def retrieve(self, key):
		return self.db.get(key, None)

	def delete(self, key):
		if key in self.db:
			del self.db[key]
			return True
		return False

	def update(self, key, value):
		if key in self.db:
			self.db[key] = value
			return True
		return False

	def get_all(self):
		return self.db
