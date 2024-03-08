from models.file import File

class FileController:
	def __init__(self):
		self.files = []

	def upload_file(self, id, name, size, owner):
		file = File(id, name, size, owner)
		self.files.append(file)
		return file

	def get_file(self, id):
		for file in self.files:
			if file.id == id:
				return file
		return None

	def update_file(self, id, name, size, owner):
		file = self.get_file(id)
		if file:
			file.name = name
			file.size = size
			file.owner = owner
			return file
		return None

	def delete_file(self, id):
		file = self.get_file(id)
		if file:
			self.files.remove(file)
			return True
		return False
