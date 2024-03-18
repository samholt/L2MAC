from datetime import datetime

# Mock database
analytics_db = {}


class Analytics:
	def __init__(self, url):
		self.url = url
		self.clicks = 0
		self.click_times = []
		self.locations = []

	def update_clicks(self, location):
		self.clicks += 1
		self.click_times.append(datetime.now())
		self.locations.append(location)

	def get_analytics(self):
		return {
			'url': self.url,
			'clicks': self.clicks,
			'click_times': self.click_times,
			'locations': self.locations
		}


# Function to get analytics for a URL
def get_url_analytics(url):
	if url in analytics_db:
		return analytics_db[url].get_analytics()
	else:
		return 'No analytics available for this URL.'


# Function to update analytics for a URL
def update_url_analytics(url, location):
	if url not in analytics_db:
		analytics_db[url] = Analytics(url)
	analytics_db[url].update_clicks(location)
