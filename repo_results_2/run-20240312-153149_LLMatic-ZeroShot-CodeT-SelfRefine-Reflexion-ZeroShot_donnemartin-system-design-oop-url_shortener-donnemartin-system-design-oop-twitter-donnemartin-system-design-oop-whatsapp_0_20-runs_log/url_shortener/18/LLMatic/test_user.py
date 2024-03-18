import pytest
from user import User
from url import URL
from analytics import update_url_analytics


def test_view_urls():
	user = User('test_user', 'password')
	url1 = URL('http://example.com', user)
	url2 = URL('http://example.org', user)
	user.urls.append(url1.short_url)
	user.urls.append(url2.short_url)
	assert user.view_urls() == [url1.short_url, url2.short_url]


def test_view_analytics():
	user = User('test_user', 'password')
	url1 = URL('http://example.com', user)
	url2 = URL('http://example.org', user)
	user.urls.append(url1.short_url)
	user.urls.append(url2.short_url)
	update_url_analytics(url1.short_url, 'USA')
	update_url_analytics(url2.short_url, 'Canada')
	analytics = user.view_analytics()
	assert analytics[url1.short_url]['clicks'] == 1
	assert analytics[url1.short_url]['locations'] == ['USA']
	assert analytics[url2.short_url]['clicks'] == 1
	assert analytics[url2.short_url]['locations'] == ['Canada']
