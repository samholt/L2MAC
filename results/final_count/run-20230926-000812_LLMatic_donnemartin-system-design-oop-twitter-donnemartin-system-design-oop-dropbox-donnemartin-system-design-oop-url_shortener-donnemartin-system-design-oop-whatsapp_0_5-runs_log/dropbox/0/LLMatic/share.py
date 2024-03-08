import random
import string
from datetime import datetime, timedelta


class Share:
	def __init__(self):
		self.shared_links = {}
		self.shared_folders = {}

	def generate_shareable_link(self, file_path, expiry_date=None, password=None):
		share_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		self.shared_links[share_id] = {
			'file_path': file_path,
			'expiry_date': expiry_date,
			'password': password
		}
		return share_id

	def get_shared_file(self, share_id, password=None):
		share_info = self.shared_links.get(share_id)
		if not share_info:
			return 'Invalid share ID'
		if share_info['expiry_date'] and share_info['expiry_date'] < datetime.now():
			return 'Link expired'
		if share_info['password'] and share_info['password'] != password:
			return 'Invalid password'
		return share_info['file_path']

	def share_folder(self, folder_path, users, permissions):
		self.shared_folders[folder_path] = {
			'users': users,
			'permissions': permissions
		}

	def get_shared_folder(self, folder_path):
		return self.shared_folders.get(folder_path)
