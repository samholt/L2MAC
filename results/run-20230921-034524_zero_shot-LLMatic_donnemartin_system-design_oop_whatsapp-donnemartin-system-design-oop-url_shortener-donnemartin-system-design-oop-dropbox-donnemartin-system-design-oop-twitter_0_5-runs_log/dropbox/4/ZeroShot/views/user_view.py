from controllers.user_controller import UserController

class UserView:
	def __init__(self):
		self.controller = UserController()

	def create_user(self, id, name, email):
		return self.controller.create_user(id, name, email)

	def get_user(self, id):
		return self.controller.get_user(id)

	def update_user(self, id, name, email):
		return self.controller.update_user(id, name, email)
