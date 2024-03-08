class Permission:
	def __init__(self, user, file, can_view=False, can_edit=False, can_share=False):
		self.user = user
		self.file = file
		self.can_view = can_view
		self.can_edit = can_edit
		self.can_share = can_share

	def grant_permission(self, user, file, permission):
		if permission == 'view':
			self.can_view = True
		elif permission == 'edit':
			self.can_edit = True
		elif permission == 'share':
			self.can_share = True
		else:
			return 'Invalid permission'

	def revoke_permission(self, user, file, permission):
		if permission == 'view':
			self.can_view = False
		elif permission == 'edit':
			self.can_edit = False
		elif permission == 'share':
			self.can_share = False
		else:
			return 'Invalid permission'

	def check_permission(self, user, file, permission):
		if permission == 'view':
			return self.can_view
		elif permission == 'edit':
			return self.can_edit
		elif permission == 'share':
			return self.can_share
		else:
			return 'Invalid permission'
