from cloudsafe.app.models import File, Folder
from datetime import datetime, timedelta


class SharingService:
	def __init__(self):
		self.share_links = {}
		self.shared_folders = {}

	def generate_share_link(self, id, file_id=None, folder_id=None, expiry_date=None, password=None):
		share_link = {'id': id, 'file_id': file_id, 'folder_id': folder_id, 'expiry_date': expiry_date, 'password': password}
		self.share_links[id] = share_link
		return 'Share link generated successfully'

	def set_expiry_date(self, id, days):
		share_link = self.share_links.get(id)
		if share_link:
			share_link['expiry_date'] = datetime.now() + timedelta(days=days)
			return 'Expiry date set successfully'
		return 'Share link not found'

	def set_password(self, id, password):
		share_link = self.share_links.get(id)
		if share_link:
			share_link['password'] = password
			return 'Password set successfully'
		return 'Share link not found'

	def invite_user(self, id, folder_id, user_id, permissions):
		shared_folder = {'id': id, 'folder_id': folder_id, 'user_id': user_id, 'permissions': permissions}
		self.shared_folders[id] = shared_folder
		return 'User invited successfully'

	def set_permissions(self, id, permissions):
		shared_folder = self.shared_folders.get(id)
		if shared_folder:
			shared_folder['permissions'] = permissions
			return 'Permissions set successfully'
		return 'Shared folder not found'

