import datetime


class Analytics:
	def __init__(self):
		self.analytics_data = {}

	def track_click(self, short_url, location):
		if short_url not in self.analytics_data:
			self.analytics_data[short_url] = {'clicks': 0, 'click_details': []}
		self.analytics_data[short_url]['clicks'] += 1
		self.analytics_data[short_url]['click_details'].append({'time': datetime.datetime.now(), 'location': location})

	def get_clicks(self, short_url):
		if short_url in self.analytics_data:
			return self.analytics_data[short_url]['clicks']
		else:
			return None

	def get_click_details(self, short_url):
		if short_url in self.analytics_data:
			return self.analytics_data[short_url]['click_details']
		else:
			return None
