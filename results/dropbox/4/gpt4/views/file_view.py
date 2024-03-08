from controllers.file_controller import FileController

class FileView:
	def __init__(self):
		self.controller = FileController()

	def upload_file(self, id, name, size, owner):
		return self.controller.upload_file(id, name, size, owner)

	def get_file(self, id):
		return self.controller.get_file(id)

	def update_file(self, id, name, size, owner):
		return self.controller.update_file(id, name, size, owner)

	def delete_file(self, id):
		return self.controller.delete_file(id)
