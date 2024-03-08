from file import File
from service import Service

class User:
	def __init__(self, user_id):
		self.user_id = user_id

	def upload_file(self, file):
		Service.upload_file(self.user_id, file)

	def view_file(self, file_id):
		return Service.view_file(self.user_id, file_id)

	def search_files(self, query):
		return Service.search_files(self.user_id, query)

	def share_file(self, file_id, recipient_id):
		Service.share_file(self.user_id, file_id, recipient_id)

	def download_file(self, file_id):
		return Service.download_file(self.user_id, file_id)
