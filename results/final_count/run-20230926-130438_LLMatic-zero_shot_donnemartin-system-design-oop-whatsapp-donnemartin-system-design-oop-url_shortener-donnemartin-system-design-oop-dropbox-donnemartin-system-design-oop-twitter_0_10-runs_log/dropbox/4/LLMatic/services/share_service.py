import random
import string

from models.share import Share


class ShareService:
	def __init__(self):
		self.shares = {}

	def generate_shareable_link(self, file, user, permissions, password=None, expiry_date=None):
		share = Share(file, user, permissions, password, expiry_date)
		share_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		self.shares[share_id] = share
		return share_id

	def generate_shareable_link_for_folder(self, folder_name, user, permissions, password=None, expiry_date=None):
		share = Share(folder_name, user, permissions, password, expiry_date)
		share_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		self.shares[share_id] = share
		return share_id
