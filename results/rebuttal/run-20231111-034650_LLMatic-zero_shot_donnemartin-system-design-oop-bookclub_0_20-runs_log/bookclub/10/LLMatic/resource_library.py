class Resource:
	def __init__(self, id, title, description, link):
		self.id = id
		self.title = title
		self.description = description
		self.link = link


class ResourceLibrary:
	def __init__(self):
		self.resources = {}

	def add_resource(self, resource):
		self.resources[resource.id] = resource

	def get_resource(self, id):
		return self.resources.get(id)

	def update_resource(self, id, title=None, description=None, link=None):
		if id in self.resources:
			if title:
				self.resources[id].title = title
			if description:
				self.resources[id].description = description
			if link:
				self.resources[id].link = link

	def delete_resource(self, id):
		if id in self.resources:
			del self.resources[id]
