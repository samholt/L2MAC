import datetime

# Mock database
analytics_db = {}


def track_click(short_url, location):
	"""Track a click for a given short URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	click_data = {
		'time': datetime.datetime.now(),
		'location': location,
	}
	analytics_db[short_url].append(click_data)


def get_click_data(short_url):
	"""Get click data for a given short URL."""
	return analytics_db.get(short_url, [])


def get_analytics_db():
	return analytics_db
