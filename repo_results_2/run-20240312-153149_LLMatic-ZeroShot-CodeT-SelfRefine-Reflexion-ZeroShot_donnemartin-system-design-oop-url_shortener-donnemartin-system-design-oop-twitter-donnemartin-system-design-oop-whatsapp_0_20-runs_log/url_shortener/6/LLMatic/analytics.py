import datetime

# Mock database
analytics_db = {}


def record_click(short_url, location='Unknown'):
	# Function to record a click event for a short URL
	if short_url not in analytics_db:
		analytics_db[short_url] = []

	click_data = {
		'time': datetime.datetime.now(),
		'location': location,
	}
	analytics_db[short_url].append(click_data)


def get_analytics(short_url):
	# Function to retrieve the analytics for a specific shortened URL
	return analytics_db.get(short_url, [])
