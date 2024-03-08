class MockDatabase:
	def __init__(self):
		self.db = {
			'User': [],
			'Message': [],
			'Group': [],
			'Status': []
		}

	def add(self, model_name, instance):
		self.db[model_name].append(instance)

	def get(self, model_name, id):
		for instance in self.db[model_name]:
			if instance.id == id:
				return instance
		return None

	def update(self, model_name, id, new_instance):
		for i, instance in enumerate(self.db[model_name]):
			if instance.id == id:
				self.db[model_name][i] = new_instance
				return True
		return False

	def delete(self, model_name, id):
		for i, instance in enumerate(self.db[model_name]):
			if instance.id == id:
				del self.db[model_name][i]
				return True
		return False
