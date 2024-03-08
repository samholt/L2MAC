import pytest
from models import User, URL, Click
from datetime import datetime, timedelta

# Mock Database
users = {}
urls = {}
clicks = {}

# Test User CRUD

def test_create_user():
	user = User('test_user', 'test_password')
	users[user.username] = user
	assert users['test_user'] == user

def test_read_user():
	assert users['test_user'].username == 'test_user'

def test_update_user():
	users['test_user'].password = 'new_password'
	assert users['test_user'].password == 'new_password'

def test_delete_user():
	del users['test_user']
	assert 'test_user' not in users

# Test URL CRUD

def test_create_url():
	user = User('test_user', 'test_password')
	users[user.username] = user
	url = URL('https://example.com', 'https://short.ly', user, datetime.now() + timedelta(days=1))
	urls[url.shortened_url] = url
	assert urls['https://short.ly'] == url

def test_read_url():
	assert urls['https://short.ly'].original_url == 'https://example.com'

def test_update_url():
	urls['https://short.ly'].original_url = 'https://newexample.com'
	assert urls['https://short.ly'].original_url == 'https://newexample.com'

def test_delete_url():
	del urls['https://short.ly']
	assert 'https://short.ly' not in urls

# Test Click CRUD

def test_create_click():
	user = User('test_user', 'test_password')
	users[user.username] = user
	url = URL('https://example.com', 'https://short.ly', user, datetime.now() + timedelta(days=1))
	urls[url.shortened_url] = url
	click = Click(url, datetime.now(), 'USA')
	clicks[click.click_time] = click
	assert clicks[click.click_time] == click

def test_read_click():
	click_time = list(clicks.keys())[0]
	assert clicks[click_time].location == 'USA'

def test_update_click():
	click_time = list(clicks.keys())[0]
	clicks[click_time].location = 'Canada'
	assert clicks[click_time].location == 'Canada'

def test_delete_click():
	click_time = list(clicks.keys())[0]
	del clicks[click_time]
	assert click_time not in clicks
