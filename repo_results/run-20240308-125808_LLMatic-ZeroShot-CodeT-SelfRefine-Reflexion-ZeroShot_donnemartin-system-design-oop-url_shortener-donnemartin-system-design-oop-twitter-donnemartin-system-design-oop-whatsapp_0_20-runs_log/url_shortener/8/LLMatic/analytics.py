import datetime

# Mock database
analytics_db = {}


def track_click(short_url, ip_address):
	"""Track a click for a given short URL."""
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	# Record click
	click_data = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address
	}
	analytics_db[short_url].append(click_data)


def get_analytics(short_url):
	"""Get analytics for a given short URL."""
	return analytics_db.get(short_url, [])
