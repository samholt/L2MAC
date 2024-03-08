from models.permission import Permission

class PermissionController:
	def __init__(self):
		self.permissions = []

	def create_permission(self, id, user, file, permission_type):
		permission = Permission(id, user, file, permission_type)
		self.permissions.append(permission)
		return permission

	def get_permission(self, id):
		for permission in self.permissions:
			if permission.id == id:
				return permission
		return None

	def update_permission(self, id, user, file, permission_type):
		permission = self.get_permission(id)
		if permission:
			permission.user = user
			permission.file = file
			permission.permission_type = permission_type
			return permission
		return None

	def delete_permission(self, id):
		permission = self.get_permission(id)
		if permission:
			self.permissions.remove(permission)
			return True
		return False
