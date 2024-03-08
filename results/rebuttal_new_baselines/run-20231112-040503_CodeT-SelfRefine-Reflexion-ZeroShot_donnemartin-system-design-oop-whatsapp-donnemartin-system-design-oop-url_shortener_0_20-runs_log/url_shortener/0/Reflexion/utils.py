import random
import string
from datetime import datetime


def generate_short_url():
	return ''.join(random.choice(string.ascii_letters) for _ in range(10))


def validate_url(url):
	# Placeholder for URL validation logic
	return True


def get_current_time():
	return datetime.now()
