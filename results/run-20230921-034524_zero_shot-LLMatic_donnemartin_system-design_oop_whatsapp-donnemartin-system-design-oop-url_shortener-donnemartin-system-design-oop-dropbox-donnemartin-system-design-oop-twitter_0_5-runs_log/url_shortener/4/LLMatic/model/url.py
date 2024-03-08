import datetime
import random
import string


class URL:
	def __init__(self, original_url, expiry_date=None, custom_alias=None):
		self.original_url = original_url
		self.short_url = self.generate_short_url(custom_alias)
		self.clicks = 0
		self.expiry_date = expiry_date

	def generate_short_url(self, custom_alias):
		if custom_alias:
			return custom_alias
		else:
			return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

	def redirect(self):
		self.clicks += 1
		return self.original_url

	def is_expired(self):
		if self.expiry_date:
			return datetime.datetime.now() > self.expiry_date
		else:
			return False
