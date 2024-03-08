import random
import string
import requests
from models import Click


# Function to validate URL
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False


# Function to generate shortened URL
def generate_shortened_url(url, custom=None):
	if custom:
		return custom
	else:
		return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# Function to gather click data
def gather_click_data(click_event):
	click_time = click_event['time']
	click_location = click_event['location']
	return Click(id=None, url_id=None, click_time=click_time, click_location=click_location)
