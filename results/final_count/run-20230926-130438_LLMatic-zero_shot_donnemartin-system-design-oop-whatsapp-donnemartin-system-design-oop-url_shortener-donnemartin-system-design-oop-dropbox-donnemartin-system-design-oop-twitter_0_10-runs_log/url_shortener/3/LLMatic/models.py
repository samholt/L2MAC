class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []


class URL:
	def __init__(self, original_url, short_url, user=None, creation_date=None, expiration_date=None):
		self.original_url = original_url
		self.short_url = short_url
		self.user = user
		self.creation_date = creation_date
		self.expiration_date = expiration_date
		self.click_events = []

	def record_click_event(self, date_time, location):
		click_event = ClickEvent(date_time, location)
		self.click_events.append(click_event)


class ClickEvent:
	def __init__(self, date_time, location):
		self.date_time = date_time
		self.location = location
