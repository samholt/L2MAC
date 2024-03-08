from datetime import datetime


class URL:
	def __init__(self, original_url, short_url, creation_date, expiration_date, click_count):
		self.original_url = original_url
		self.short_url = short_url
		self.creation_date = creation_date
		self.expiration_date = expiration_date
		self.click_count = click_count

