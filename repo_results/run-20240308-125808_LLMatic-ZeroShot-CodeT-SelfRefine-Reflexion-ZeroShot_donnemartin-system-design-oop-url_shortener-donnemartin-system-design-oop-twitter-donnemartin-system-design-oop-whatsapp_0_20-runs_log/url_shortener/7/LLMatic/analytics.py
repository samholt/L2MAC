import datetime

# Mock database
analytics_data = {}

def track_click(short_url, ip_address):
	"""Track a click for a given short URL."""
	if short_url not in analytics_data:
		analytics_data[short_url] = []

	# Record click data
	click_data = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address,
	}
	analytics_data[short_url].append(click_data)


def get_click_data(short_url):
	"""Retrieve click data for a given short URL."""
	return analytics_data.get(short_url, [])
