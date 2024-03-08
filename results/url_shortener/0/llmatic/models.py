from datetime import datetime


class URL:
	def __init__(self, original_url, short_url, creation_date=None, click_count=0):
		self.original_url = original_url
		self.short_url = short_url
		self.creation_date = creation_date if creation_date else datetime.now()
		self.click_count = click_count

	def increment_click_count(self):
		self.click_count += 1

