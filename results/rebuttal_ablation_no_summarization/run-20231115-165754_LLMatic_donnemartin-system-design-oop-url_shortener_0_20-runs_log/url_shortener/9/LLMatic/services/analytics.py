import datetime


class Analytics:
	def __init__(self):
		# Initialize analytics data
		self.analytics_data = {}

	def record_click(self, short_url, location):
		# Record a click on a short URL
		if short_url not in self.analytics_data:
			self.analytics_data[short_url] = {'clicks': 0, 'click_details': []}
		self.analytics_data[short_url]['clicks'] += 1
		self.analytics_data[short_url]['click_details'].append({'time': datetime.datetime.now(), 'location': location})

	def get_click_data(self, short_url):
		# Get click data for a short URL
		return self.analytics_data.get(short_url, 'No data available for this URL')

	def get_all_data(self):
		# Get all analytics data
		return self.analytics_data

