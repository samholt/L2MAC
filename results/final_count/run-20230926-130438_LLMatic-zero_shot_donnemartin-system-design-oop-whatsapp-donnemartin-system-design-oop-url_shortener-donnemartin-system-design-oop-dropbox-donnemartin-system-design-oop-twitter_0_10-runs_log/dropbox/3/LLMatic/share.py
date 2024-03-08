import uuid
import datetime

class Share:
	def __init__(self):
		self.shared_links = {}
		self.shared_folders = {}

	def generate_shareable_link(self, file_path, expiry_date=None, password=None):
		link_id = str(uuid.uuid4())
		self.shared_links[link_id] = {
			'file_path': file_path,
			'expiry_date': expiry_date,
			'password': password
		}
		return link_id

	def get_shared_link(self, link_id, password=None):
		link = self.shared_links.get(link_id)
		if link and (not link['expiry_date'] or link['expiry_date'] > datetime.datetime.now()) and (not link['password'] or link['password'] == password):
			return link['file_path']
		return None

	def invite_to_folder(self, folder_path, user, permissions):
		if folder_path not in self.shared_folders:
			self.shared_folders[folder_path] = {}
		self.shared_folders[folder_path][user] = permissions

	def get_folder_permissions(self, folder_path, user):
		if folder_path in self.shared_folders and user in self.shared_folders[folder_path]:
			return self.shared_folders[folder_path][user]
		return None

	def share_file(self, file_name, email):
		self.shared_links[str(uuid.uuid4())] = {
			'file_path': file_name,
			'email': email
		}
