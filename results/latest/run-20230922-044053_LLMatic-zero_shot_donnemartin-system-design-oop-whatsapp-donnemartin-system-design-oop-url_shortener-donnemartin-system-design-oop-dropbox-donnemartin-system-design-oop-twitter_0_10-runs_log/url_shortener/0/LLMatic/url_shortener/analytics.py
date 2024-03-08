from typing import List
from .models import URL, Click

# In-memory database
DB = {}

def get_clicks(url: URL) -> List[Click]:
	# Retrieve Click objects from the database using the URL
	return DB.get(url.shortened_url, [])

