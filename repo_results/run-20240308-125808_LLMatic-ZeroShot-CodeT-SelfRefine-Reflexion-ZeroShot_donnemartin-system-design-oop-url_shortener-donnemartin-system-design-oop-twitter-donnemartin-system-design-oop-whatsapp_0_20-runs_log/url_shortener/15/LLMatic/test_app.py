import pytest
import app
import mock_db
from datetime import datetime, timedelta
from flask import Flask, json

app.app = Flask(__name__)


def test_shorten_url():
	app.db = mock_db.MockDB()
	with app.app.test_request_context(json={'url': 'http://example.com'}):
		response = app.shorten_url()
		assert response[1] == 201
		assert 'short_url' in response[0].json

	with app.app.test_request_context(json={'url': 'invalid'}):
		response = app.shorten_url()
		assert response[1] == 400

	with app.app.test_request_context(json={'url': 'http://example.com', 'custom_short_link': 'custom'}):
		response = app.shorten_url()
		assert response[1] == 201

	with app.app.test_request_context(json={'url': 'http://example.com', 'custom_short_link': 'custom'}):
		response = app.shorten_url()
		assert response[1] == 400

	with app.app.test_request_context(json={'url': 'http://google.com'}):
		response = app.shorten_url()
		assert response[1] == 201


def test_redirect_url():
	app.db = mock_db.MockDB()
	short_url = app.db.add_url('http://example.com')
	with app.app.test_request_context(path='/' + short_url):
		response = app.redirect_url(short_url)
		assert response.status_code == 302

	with app.app.test_request_context(path='/invalid'):
		response = app.redirect_url('invalid')
		assert response[1] == 404


def test_analytics():
	app.db = mock_db.MockDB()
	short_url = app.db.add_url('http://example.com')
	with app.app.test_request_context(path='/analytics/' + short_url):
		response = app.analytics(short_url)
		assert response[1] == 200

	with app.app.test_request_context(path='/analytics/invalid'):
		response = app.analytics('invalid')
		assert response[1] == 200


def test_account():
	app.db = mock_db.MockDB()
	with app.app.test_request_context(json={'username': 'user', 'password': 'pass'}):
		response = app.account()
		assert response[1] == 200

	with app.app.test_request_context():
		response = app.account()
		assert response[1] == 200

	with app.app.test_request_context(json={'user_id': 'invalid', 'username': 'user', 'password': 'pass'}):
		response = app.account()
		assert response[1] == 200

	with app.app.test_request_context(json={'user_id': 'invalid'}):
		response = app.account()
		assert response[1] == 200


def test_admin():
	app.db = mock_db.MockDB()
	with app.app.test_request_context():
		response = app.admin()
		assert response[1] == 200

	with app.app.test_request_context(json={'user_id': 'invalid'}):
		response = app.admin()
		assert response[1] == 200


def test_admin_analytics():
	app.db = mock_db.MockDB()
	with app.app.test_request_context():
		response = app.admin_analytics()
		assert response[1] == 200


def test_url_expiration():
	app.db = mock_db.MockDB()
	expiration_date = (datetime.now() + timedelta(days=1)).isoformat()
	short_url = app.db.add_url('http://example.com', expiration_date=expiration_date)
	with app.app.test_request_context(path='/' + short_url):
		response = app.redirect_url(short_url)
		assert response.status_code == 302

	expiration_date = (datetime.now() - timedelta(days=1)).isoformat()
	short_url = app.db.add_url('http://example.com', expiration_date=expiration_date)
	with app.app.test_request_context(path='/' + short_url):
		response = app.redirect_url(short_url)
		assert response[1] == 404


def test_analytics_update():
	app.db = mock_db.MockDB()
	short_url = app.db.add_url('http://example.com')
	with app.app.test_request_context(path='/' + short_url):
		response = app.redirect_url(short_url)
		assert response.status_code == 302
		analytics = app.db.get_analytics(short_url)
		assert analytics['clicks'] == 1
		assert len(analytics['click_data']) == 1
		assert 'time' in analytics['click_data'][0]
		assert 'location' in analytics['click_data'][0]
		assert analytics['click_data'][0]['location'] == 'Unknown'

	with app.app.test_request_context(path='/' + short_url):
		response = app.redirect_url(short_url)
		assert response.status_code == 302
		analytics = app.db.get_analytics(short_url)
		assert analytics['clicks'] == 2
		assert len(analytics['click_data']) == 2
		assert 'time' in analytics['click_data'][1]
		assert 'location' in analytics['click_data'][1]
		assert analytics['click_data'][1]['location'] == 'Unknown'

