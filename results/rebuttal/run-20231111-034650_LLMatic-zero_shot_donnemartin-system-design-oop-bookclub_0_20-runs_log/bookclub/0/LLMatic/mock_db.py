class MockDB:
	def __init__(self):
		self.users = {}
		self.book_clubs = {}
		self.meetings = {}
		self.discussions = {}
		self.books = {}
		self.notifications = {}

	def add(self, table, key, value):
		table[key] = value

	def get(self, table, key):
		return table.get(key)

	def update(self, table, key, value):
		if key in table:
			table[key] = value

	def delete(self, table, key):
		if key in table:
			del table[key]
