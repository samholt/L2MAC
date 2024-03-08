import datetime


class Analytics:
	def __init__(self):
		self.data = {}

	def track_click(self, short_url, location):
		if short_url not in self.data:
			self.data[short_url] = []
		self.data[short_url].append({
			'time': datetime.datetime.now(),
			'location': location
		})

	def get_click_data(self, short_url):
		return self.data.get(short_url, [])
