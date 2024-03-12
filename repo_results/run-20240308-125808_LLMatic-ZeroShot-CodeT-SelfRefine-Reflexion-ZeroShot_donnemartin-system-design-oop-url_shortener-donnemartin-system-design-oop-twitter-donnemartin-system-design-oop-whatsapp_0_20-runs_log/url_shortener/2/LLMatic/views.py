from flask import request, jsonify, redirect
from models import URL, ClickEvent
from utils import validate_url, generate_short_link
from datetime import datetime

# Mock database
DATABASE = {}


def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	custom_short_link = data.get('custom_short_link')

	if not validate_url(original_url):
		return jsonify({'error': 'Invalid URL'}), 400

	short_link = custom_short_link if custom_short_link else generate_short_link()

	url = URL(original_url=original_url, shortened_url=short_link)
	DATABASE[short_link] = url

	return jsonify({'short_link': short_link}), 200


def redirect_url(short_link):
	url = DATABASE.get(short_link)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Record a new click event
	click_event = ClickEvent(date_time=datetime.utcnow(), location=request.remote_addr)
	url.click_events.append(click_event)

	# Redirect to the original URL
	return redirect(url.original_url, code=302)


def get_url_stats(short_link):
	url = DATABASE.get(short_link)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	click_events = [{'date_time': str(event.date_time), 'location': event.location} for event in url.click_events]

	return jsonify({'short_link': short_link, 'clicks': len(click_events), 'click_events': click_events}), 200
