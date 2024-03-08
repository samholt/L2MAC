from user import User
from file import File
from folder import Folder
from permission import Permission
from database import Database

class Controller:
	def __init__(self, db_name):
		self.database = Database(db_name)
		self.users = {}

	def create_user(self, username, password):
		user = User(username, password)
		self.users[username] = user
		return user

	def upload_file(self, username, file_name, file_size, file_content):
		user = self.users.get(username)
		if user:
			file = File(file_name, file_size, file_content)
			file_id = user.upload_file(file)
			return file
		return None

	def view_file(self, username, file_id):
		user = self.users.get(username)
		if user:
			return user.view_file(file_id)
		return None

	def search_file(self, username, file_name):
		user = self.users.get(username)
		if user:
			return user.search_file(file_name)
		return None

	def share_file(self, username, file_id, other_username, permission):
		user = self.users.get(username)
		other_user = self.users.get(other_username)
		if user and other_user:
			user.share_file(file_id, other_user, permission)
			return True
		return False

	def download_file(self, username, file_id):
		user = self.users.get(username)
		if user:
			return user.download_file(file_id)
		return None
