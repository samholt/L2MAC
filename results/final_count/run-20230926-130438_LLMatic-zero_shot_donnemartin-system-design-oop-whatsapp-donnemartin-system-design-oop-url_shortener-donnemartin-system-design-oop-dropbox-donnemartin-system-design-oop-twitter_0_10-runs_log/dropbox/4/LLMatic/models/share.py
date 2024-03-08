class Share:
	def __init__(self, file, user, permissions, password=None, expiry_date=None):
		self.file = file
		self.user = user
		self.permissions = permissions
		self.password = password
		self.expiry_date = expiry_date
