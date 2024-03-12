class Database:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Database, cls).__new__(cls)
			cls._instance.users = {}
			cls._instance.urls = {}
			cls._instance.analytics = {}
		return cls._instance

	def insert(self, table, key, value):
		if table == 'users':
			self.users[key] = value
		elif table == 'urls':
			self.urls[key] = value
		elif table == 'analytics':
			self.analytics[key] = value

	def get(self, table, key):
		if table == 'users':
			return self.users.get(key)
		elif table == 'urls':
			return self.urls.get(key)
		elif table == 'analytics':
			return self.analytics.get(key)

	def update(self, table, key, value):
		if table == 'users' and key in self.users:
			self.users[key] = value
		elif table == 'urls' and key in self.urls:
			self.urls[key] = value
		elif table == 'analytics' and key in self.analytics:
			self.analytics[key] = value

	def delete(self, table, key):
		if table == 'users' and key in self.users:
			del self.users[key]
		elif table == 'urls' and key in self.urls:
			del self.urls[key]
		elif table == 'analytics' and key in self.analytics:
			del self.analytics[key]
