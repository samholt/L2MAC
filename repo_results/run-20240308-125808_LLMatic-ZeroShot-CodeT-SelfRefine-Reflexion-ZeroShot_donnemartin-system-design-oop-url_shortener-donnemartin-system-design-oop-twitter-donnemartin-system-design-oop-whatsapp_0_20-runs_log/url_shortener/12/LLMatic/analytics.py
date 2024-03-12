import datetime

# Mock database
analytics_data = {}


def track_click(short_url, ip_address):
	"""Track each click for a short URL."""
	if short_url not in analytics_data:
		analytics_data[short_url] = []

	# Store click data
	click_data = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address
	}
	analytics_data[short_url].append(click_data)


def get_analytics(short_url):
	"""Retrieve analytics data for a short URL."""
	return analytics_data.get(short_url, [])
