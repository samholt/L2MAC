class Database:
	def __init__(self):
		self.data = {}

	def insert(self, table, record):
		if table not in self.data:
			self.data[table] = []
		record['id'] = len(self.data[table])
		self.data[table].append(record)
		return record['id']

	def get(self, table, id):
		if table in self.data:
			for record in self.data[table]:
				if record['id'] == id:
					return record
		return None

	def get_all(self, table):
		return self.data.get(table, [])

	def update(self, table, id, record):
		if table in self.data:
			for i, existing_record in enumerate(self.data[table]):
				if existing_record['id'] == id:
					self.data[table][i] = {**existing_record, **record}
					return True
		return False

	def delete(self, table, id):
		if table in self.data:
			for i, existing_record in enumerate(self.data[table]):
				if existing_record['id'] == id:
					self.data[table].pop(i)
					return True
		return False

	def get_user_activities(self):
		return self.get_all('user_activities')

	def get_system_performance(self):
		return self.get_all('system_performance')

	def get_vendor_listings(self):
		return self.get_all('vendor_listings')
