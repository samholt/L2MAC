import datetime

# Mock database
analytics_data = {}


def track_click(short_url, ip_address):
	"""Track a click event."""
	if short_url not in analytics_data:
		analytics_data[short_url] = []

	# Record the click event
	click_event = {
		'time': datetime.datetime.now(),
		'ip_address': ip_address
	}
	analytics_data[short_url].append(click_event)


def get_analytics(short_url):
	"""Retrieve analytics data for a short URL."""
	return analytics_data.get(short_url, [])


def get_system_performance():
	"""Retrieve system performance data.

	Returns:
		dict: A dictionary containing system performance data.
	"""
	# For simplicity, we'll just return the number of URLs and the number of click events.
	return {
		'num_urls': len(analytics_data),
		'num_clicks': sum(len(events) for events in analytics_data.values())
	}
