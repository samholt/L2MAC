import pytest
from views import shorten_url, redirect_url, get_url_stats
from models import URL, ClickEvent
from datetime import datetime
from flask import Flask, jsonify

# Mock database
DATABASE = {}

app = Flask(__name__)


def test_shorten_url():
	with app.test_request_context(json={'original_url': 'https://www.google.com'}):
		response = shorten_url()
		assert response[1] == 200
		assert 'short_link' in response[0].get_json()


def test_redirect_url():
	short_link = 'test_link'
	url = URL(original_url='https://www.google.com', shortened_url=short_link)
	DATABASE[short_link] = url

	with app.test_request_context(path=short_link):
		response = redirect_url(short_link)
		assert response[1] == 302


def test_get_url_stats():
	short_link = 'test_link'
	url = URL(original_url='https://www.google.com', shortened_url=short_link)
	click_event = ClickEvent(date_time=datetime.utcnow(), location='127.0.0.1')
	url.click_events.append(click_event)
	DATABASE[short_link] = url

	with app.test_request_context(path=short_link):
		response = get_url_stats(short_link)
		assert response[1] == 200
		assert 'short_link' in response[0].get_json()
		assert 'clicks' in response[0].get_json()
		assert 'click_events' in response[0].get_json()
		assert response[0].get_json()['clicks'] == 1
		assert response[0].get_json()['click_events'][0]['date_time'] == str(click_event.date_time)
		assert response[0].get_json()['click_events'][0]['location'] == click_event.location
