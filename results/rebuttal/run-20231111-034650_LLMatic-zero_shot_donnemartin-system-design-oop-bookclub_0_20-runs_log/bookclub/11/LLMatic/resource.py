class Resource:
	def __init__(self):
		self.resources = {}

	def add_resource(self, title, content):
		self.resources[title] = content

	def view_resources(self):
		return self.resources
