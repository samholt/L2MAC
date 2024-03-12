import datetime

# Mock database
analytics_db = {}


def track_click(short_url, location):
	"""Track a click for a shortened URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	click_data = {
		'date_time': datetime.datetime.now(),
		'location': location,
	}
	analytics_db[short_url].append(click_data)


def get_click_data(short_url):
	"""Retrieve click data for a shortened URL."""
	return analytics_db.get(short_url, [])
