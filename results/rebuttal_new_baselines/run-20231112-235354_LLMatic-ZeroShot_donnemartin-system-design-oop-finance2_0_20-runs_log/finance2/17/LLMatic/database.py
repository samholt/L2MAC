class MockDatabase:
	def __init__(self):
		self.users = {}
		self.expenses = {}
		self.incomes = {}
		self.budgets = {}
		self.investments = {}
		self.reports = {}

	def add(self, table, id, data):
		if table not in self.__dict__:
			return 'Invalid table'
		self.__dict__[table][id] = data
		return 'Data added successfully'

	def get(self, table, id):
		if table not in self.__dict__ or id not in self.__dict__[table]:
			return 'Invalid table or id'
		return self.__dict__[table][id]

	def update(self, table, id, data):
		if table not in self.__dict__ or id not in self.__dict__[table]:
			return 'Invalid table or id'
		self.__dict__[table][id] = data
		return 'Data updated successfully'

	def delete(self, table, id):
		if table not in self.__dict__ or id not in self.__dict__[table]:
			return 'Invalid table or id'
		del self.__dict__[table][id]
		return 'Data deleted successfully'
