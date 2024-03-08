class ResourceLibrary:
	def __init__(self):
		self.library = {}

	def share_resource(self, user, resource):
		if user not in self.library:
			self.library[user] = []
		self.library[user].append(resource)
		return 'Resource shared successfully'

	def contribute_to_library(self, user, resource):
		if 'contributions' not in self.library:
			self.library['contributions'] = []
		self.library['contributions'].append({user: resource})
		return 'Resource contributed successfully'
