from controller import Controller
class View:
	def __init__(self, controller):
		self.controller = controller

	def create_user(self, username, password):
		return self.controller.create_user(username, password)

	def upload_file(self, username, file_name, file_size, file_content):
		return self.controller.upload_file(username, file_name, file_size, file_content)

	def view_file(self, username, file_id):
		return self.controller.view_file(username, file_id)

	def search_file(self, username, file_name):
		return self.controller.search_file(username, file_name)

	def share_file(self, username, file_id, other_username, permission):
		return self.controller.share_file(username, file_id, other_username, permission)

	def download_file(self, username, file_id):
		return self.controller.download_file(username, file_id)
