class Resource:
	def __init__(self, title, content, contributor):
		self.title = title
		self.content = content
		self.contributor = contributor

	def add_resource(self, title, content, contributor):
		self.title = title
		self.content = content
		self.contributor = contributor

	def update_resource(self, title=None, content=None, contributor=None):
		if title:
			self.title = title
		if content:
			self.content = content
		if contributor:
			self.contributor = contributor

	def contribute(self, contribution):
		self.content += contribution
