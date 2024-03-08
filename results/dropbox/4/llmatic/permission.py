class Permission:
	def __init__(self, read, write, share):
		self.read = read
		self.write = write
		self.share = share

	def check_permission(self, permission_type):
		if permission_type == 'read':
			return self.read
		elif permission_type == 'write':
			return self.write
		elif permission_type == 'share':
			return self.share
		else:
			return False

	def set_permission(self, permission_type, value):
		if permission_type == 'read':
			self.read = value
		elif permission_type == 'write':
			self.write = value
		elif permission_type == 'share':
			self.share = value
		else:
			raise ValueError('Invalid permission type')

