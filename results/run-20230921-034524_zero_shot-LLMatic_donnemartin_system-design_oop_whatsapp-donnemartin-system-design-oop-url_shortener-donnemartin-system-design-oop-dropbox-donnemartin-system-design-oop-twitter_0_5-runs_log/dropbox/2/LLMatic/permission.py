class Permission:
	def __init__(self, user, access_type):
		self.user = user
		self.access_type = access_type

	def check_permission(self, user):
		return self.user == user

	def change_permission(self, user, access_type):
		self.user = user
		self.access_type = access_type
