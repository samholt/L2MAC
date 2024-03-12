class Analytics:
	def __init__(self):
		self.data = {}

	def track(self, short_url, timestamp, location):
		if short_url not in self.data:
			self.data[short_url] = []
		self.data[short_url].append({'timestamp': timestamp, 'location': location})

	def retrieve(self, short_url):
		return self.data.get(short_url, [])
