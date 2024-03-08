from database import DATABASE

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}

	def get_shortened_urls(self):
		return list(self.urls.keys())

	def edit_url(self, old_short_url, new_short_url):
		if old_short_url in self.urls:
			self.urls[new_short_url] = self.urls.pop(old_short_url)

	def delete_url(self, short_url):
		if short_url in self.urls:
			del self.urls[short_url]

	def get_analytics(self, short_url):
		if short_url in self.urls:
			return self.urls[short_url].get_analytics()

class URL:
	def __init__(self, original_url, short_url, user, expiration_date):
		self.original_url = original_url
		self.short_url = short_url
		self.user = user
		self.expiration_date = expiration_date
		self.clicks = []

	def add_click(self, click):
		self.clicks.append(click)

	def get_analytics(self):
		return {
			'clicks': len(self.clicks),
			'click_dates': [click.date for click in self.clicks],
			'click_geolocations': [click.geolocation for click in self.clicks]
		}

class Click:
	def __init__(self, url, date, geolocation):
		self.url = url
		self.date = date
		self.geolocation = geolocation

