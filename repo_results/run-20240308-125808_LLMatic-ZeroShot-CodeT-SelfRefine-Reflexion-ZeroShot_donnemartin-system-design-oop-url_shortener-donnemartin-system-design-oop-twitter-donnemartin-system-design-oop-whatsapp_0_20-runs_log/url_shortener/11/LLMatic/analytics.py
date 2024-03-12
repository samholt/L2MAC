import datetime

# Mock database
analytics_data = {}


def track_click(short_url, location):
	"""Track the click for a given short URL."""
	if short_url not in analytics_data:
		analytics_data[short_url] = []

	click_data = {
		'time': datetime.datetime.now(),
		'location': location,
	}
	analytics_data[short_url].append(click_data)


def get_analytics(short_url):
	"""Get the analytics for a given short URL."""
	return analytics_data.get(short_url, [])
