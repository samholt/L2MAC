import datetime

# Mock database
ANALYTICS_DB = {}


class Analytics:
	def __init__(self):
		self.ANALYTICS_DB = ANALYTICS_DB

	def track_click(self, short_url, ip_address):
		click_info = {
			'date_time': datetime.datetime.now(),
			'ip_address': ip_address
		}
		if short_url in self.ANALYTICS_DB:
			self.ANALYTICS_DB[short_url].append(click_info)
		else:
			self.ANALYTICS_DB[short_url] = [click_info]

	def get_analytics(self, short_url):
		return self.ANALYTICS_DB.get(short_url, [])
