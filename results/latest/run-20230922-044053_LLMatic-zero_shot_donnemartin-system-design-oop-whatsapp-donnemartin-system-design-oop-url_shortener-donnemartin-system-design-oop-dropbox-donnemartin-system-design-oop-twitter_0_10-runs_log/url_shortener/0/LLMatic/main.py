from flask import Flask, redirect
from url_shortener import models, shortener, validator, analytics, user_management, admin

app = Flask(__name__)

DB = {'urls': [], 'clicks': []}

@app.route('/<short_code>')
def redirect_to_url(short_code):
	# Retrieve the URL object from the database
	url = next((url for url in DB.get('urls', []) if url.shortened_url.endswith(short_code)), None)
	if url is None or url.is_expired():
		return 'URL not found or expired', 404
	# Create a Click object in the database
	click = models.Click(url, datetime.now())
	DB.setdefault('clicks', []).append(click)
	return redirect(url.original_url)
