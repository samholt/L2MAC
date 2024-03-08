class Analytics:
	def __init__(self):
		self.data = {}

	def record(self, short_url):
		if short_url not in self.data:
			self.data[short_url] = 0
		self.data[short_url] += 1

	def retrieve(self, short_url):
		return self.data.get(short_url, 0)
