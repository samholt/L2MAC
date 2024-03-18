import string
import random
from datetime import datetime, timedelta


class URL:
	def __init__(self, original_url, user, expiration_date=None):
		self.original_url = original_url
		self.short_url = self.generate_short_url()
		self.user = user
		self.expiration_date = expiration_date

	@staticmethod
	def generate_short_url():
		return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	def is_valid(self):
		# This is a simple validation. In a real world scenario, we would use a more comprehensive validation
		return self.original_url.startswith('http')

	def is_expired(self):
		if self.expiration_date:
			return datetime.now() > self.expiration_date
		return False

	def redirect(self):
		# In a real world scenario, we would use a HTTP redirection here
		return self.original_url
