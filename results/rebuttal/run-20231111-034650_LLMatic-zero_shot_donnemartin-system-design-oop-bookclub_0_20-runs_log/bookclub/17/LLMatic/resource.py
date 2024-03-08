class Resource:
	def __init__(self, db):
		self.db = db

	def add_resource(self, resource):
		self.db['resources'].append(resource)

	def get_resources(self):
		return self.db['resources']

	def update_resource(self, resource_id, updated_resource):
		for i, resource in enumerate(self.db['resources']):
			if resource['id'] == resource_id:
				self.db['resources'][i] = updated_resource
				return True
		return False

	def delete_resource(self, resource_id):
		for i, resource in enumerate(self.db['resources']):
			if resource['id'] == resource_id:
				del self.db['resources'][i]
				return True
		return False
