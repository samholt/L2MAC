import datetime


class Analytics:
	def __init__(self):
		self.data = {}

	def record_click(self, short_url, location):
		if short_url not in self.data:
			self.data[short_url] = []
		self.data[short_url].append({
			'time': datetime.datetime.now(),
			'location': location
		})

	def get_statistics(self, short_url):
		return self.data.get(short_url, [])
