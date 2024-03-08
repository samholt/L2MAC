class Database:
	def __init__(self):
		self.users = {}
		self.book_clubs = {}
		self.meetings = {}
		self.discussions = {}
		self.books = {}
		self.notifications = {}

	def insert(self, table, id, record):
		table[id] = record

	def get(self, table, id):
		return table.get(id, None)

	def delete(self, table, id):
		if id in table:
			del table[id]
