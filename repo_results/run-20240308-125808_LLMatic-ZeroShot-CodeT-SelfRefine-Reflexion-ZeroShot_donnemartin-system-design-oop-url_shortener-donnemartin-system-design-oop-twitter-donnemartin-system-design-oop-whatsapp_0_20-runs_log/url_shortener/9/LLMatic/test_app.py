import pytest
import app
import json
from flask import Flask
from werkzeug.test import Client

app.app = Flask(__name__)
client = Client(app.app)


def test_view_all_urls():
	app.url_db['test_url'] = 'http://example.com'
	response = client.get('/admin/view_urls')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'test_url' in data


def test_delete_url():
	app.url_db['test_url'] = 'http://example.com'
	response = client.post('/admin/delete_url', data={'short_url': 'test_url'})
	assert response.status_code == 200
	assert 'test_url' not in app.url_db


def test_delete_user():
	app.user_accounts.users['test_user'] = 'password'
	response = client.post('/admin/delete_user', data={'username': 'test_user'})
	assert response.status_code == 200
	assert 'test_user' not in app.user_accounts.users


def test_view_analytics():
	app.analytics_db['test_url'] = [{'time': '2022-01-01T00:00:00', 'ip_address': '127.0.0.1'}]
	response = client.get('/admin/view_analytics/test_url')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data[0]['time'] == '2022-01-01T00:00:00'
	assert data[0]['ip_address'] == '127.0.0.1'

if __name__ == '__main__':
	pytest.main()

