from controllers.permission_controller import PermissionController

class PermissionView:
	def __init__(self):
		self.controller = PermissionController()

	def create_permission(self, id, user, file, permission_type):
		return self.controller.create_permission(id, user, file, permission_type)

	def get_permission(self, id):
		return self.controller.get_permission(id)

	def update_permission(self, id, user, file, permission_type):
		return self.controller.update_permission(id, user, file, permission_type)

	def delete_permission(self, id):
		return self.controller.delete_permission(id)
