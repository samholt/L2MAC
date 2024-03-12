import datetime
from collections import defaultdict

# Mock database
analytics_db = defaultdict(list)


def record_click(short_url, ip_address):
	"""Record a click event."""
	# Get current date and time
	current_time = datetime.datetime.now()
	
	# Mock geographical location from IP address
	location = 'Mock Location'
	
	# Record click event
	analytics_db[short_url].append((current_time, location))


def get_click_count(short_url):
	"""Get the number of clicks for a specific shortened URL."""
	return len(analytics_db[short_url])


def get_click_details(short_url):
	"""Get the details of each click for a specific shortened URL."""
	return analytics_db[short_url]
