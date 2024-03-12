from datetime import datetime


class Analytics:
	def __init__(self):
		self.data = {}

	def track_click(self, short_url, location):
		if short_url not in self.data:
			self.data[short_url] = []
		self.data[short_url].append({'timestamp': datetime.now(), 'location': location})
		return 'Click tracked successfully'

	def get_statistics(self, short_url):
		return self.data.get(short_url, [])

